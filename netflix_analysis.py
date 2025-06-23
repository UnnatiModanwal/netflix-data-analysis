import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
try:
    df = pd.read_csv('netflix_titles.csv')
    print("Dataset loaded successfully!")

    # --- Data Cleaning ---
    # Fill missing 'director', 'cast', 'country' with 'Unknown'
    for col in ['director', 'cast', 'country']:
        df[col] = df[col].fillna('Unknown')

    # Drop rows with missing 'date_added'
    df.dropna(subset=['date_added'], inplace=True)

    # Fill missing 'rating' with the mode
    df['rating'] = df['rating'].fillna(df['rating'].mode()[0])

    # Handle 'duration' column
    # Separate movies and TV shows
    movies_df = df[df['type'] == 'Movie'].copy()
    tv_shows_df = df[df['type'] == 'TV Show'].copy()

    # Process movie durations
    movies_df['duration'] = movies_df['duration'].str.replace(' min', '').astype(float)
    movies_df.rename(columns={'duration': 'duration_minutes'}, inplace=True)
    
    # Handle missing duration values in movies_df by filling with the mean
    movies_df['duration_minutes'] = movies_df['duration_minutes'].fillna(movies_df['duration_minutes'].mean())

    tv_shows_df['duration'] = tv_shows_df['duration'].str.replace(' Season[s]?', '', regex=True).astype(float)
    tv_shows_df.rename(columns={'duration': 'duration_seasons'}, inplace=True)
    
    # Handle missing duration values in tv_shows_df by filling with the mean
    tv_shows_df['duration_seasons'] = tv_shows_df['duration_seasons'].fillna(tv_shows_df['duration_seasons'].mean())

    # Recombine the dataframes
    df = pd.concat([movies_df, tv_shows_df], ignore_index=True)

    # Convert 'date_added' to datetime objects
    df['date_added'] = pd.to_datetime(df['date_added'], format='mixed')

    print("\nDataset after cleaning:")
    print("First 5 rows:")
    print(df.head())
    print("\nDataset Information after cleaning:")
    df.info()
    print("\nMissing values after cleaning:")
    print(df.isnull().sum())

    # --- Exploratory Data Analysis (EDA) and Visualization ---

    # 1. Content Type Distribution
    plt.figure(figsize=(8, 6))
    sns.countplot(x='type', data=df, palette='viridis', hue='type', legend=False)
    plt.title('Distribution of Content Types')
    plt.xlabel('Content Type')
    plt.ylabel('Count')
    plt.savefig('content_type_distribution.png')
    plt.close()
    print("Generated: content_type_distribution.png")

    # 2. Content Added Over Time
    df['year_added'] = df['date_added'].dt.year
    content_added_per_year = df.groupby('year_added').size().reset_index(name='count')
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='year_added', y='count', data=content_added_per_year, marker='o')
    plt.title('Number of Content Added Over Time')
    plt.xlabel('Year Added')
    plt.ylabel('Number of Titles')
    plt.grid(True)
    plt.savefig('content_added_over_time.png')
    plt.close()
    print("Generated: content_added_over_time.png")

    # 3. Top Countries
    # Exclude 'Unknown' country for this analysis
    top_countries = df[df['country'] != 'Unknown']['country'].value_counts().head(10)
    plt.figure(figsize=(12, 7))
    sns.barplot(x=top_countries.values, y=top_countries.index, palette='magma', hue=top_countries.index, legend=False)
    plt.title('Top 10 Content-Producing Countries')
    plt.xlabel('Number of Titles')
    plt.ylabel('Country')
    plt.savefig('top_countries.png')
    plt.close()
    print("Generated: top_countries.png")

    # 4. Top Directors
    # Exclude 'Unknown' director for this analysis
    top_directors = df[df['director'] != 'Unknown']['director'].value_counts().head(10)
    plt.figure(figsize=(12, 7))
    sns.barplot(x=top_directors.values, y=top_directors.index, palette='cubehelix', hue=top_directors.index, legend=False)
    plt.title('Top 10 Directors on Netflix')
    plt.xlabel('Number of Titles')
    plt.ylabel('Director')
    plt.savefig('top_directors.png')
    plt.close()
    print("Generated: top_directors.png")

    # 5. Top Actors (Cast)
    # Exclude 'Unknown' cast for this analysis and split by ', '
    cast_df = df[df['cast'] != 'Unknown']['cast'].str.split(', ', expand=True).stack().reset_index(drop=True)
    top_actors = cast_df.value_counts().head(10)
    plt.figure(figsize=(12, 7))
    sns.barplot(x=top_actors.values, y=top_actors.index, palette='rocket', hue=top_actors.index, legend=False)
    plt.title('Top 10 Actors on Netflix')
    plt.xlabel('Number of Titles')
    plt.ylabel('Actor')
    plt.savefig('top_actors.png')
    plt.close()
    print("Generated: top_actors.png")

    # 6. Distribution of Content Ratings
    plt.figure(figsize=(10, 6))
    sns.countplot(x='rating', data=df, order=df['rating'].value_counts().index, palette='coolwarm')
    plt.title('Distribution of Content Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('content_ratings_distribution.png')
    plt.close()
    print("Generated: content_ratings_distribution.png")

    # 7. Top Genres/Categories
    genres_df = df['listed_in'].str.split(', ', expand=True).stack().reset_index(drop=True)
    top_genres = genres_df.value_counts().head(10)
    plt.figure(figsize=(12, 7))
    sns.barplot(x=top_genres.values, y=top_genres.index, palette='viridis')
    plt.title('Top 10 Genres/Categories on Netflix')
    plt.xlabel('Number of Titles')
    plt.ylabel('Genre/Category')
    plt.savefig('top_genres.png')
    plt.close()
    print("Generated: top_genres.png")

    # 8. Release Year vs. Year Added (Trend)
    # Create a DataFrame for counts of release_year and year_added
    release_year_counts = df.groupby('release_year').size().reset_index(name='release_count')
    year_added_counts = df.groupby('year_added').size().reset_index(name='added_count')

    # Merge for plotting
    # We need to ensure that the merge operation correctly handles the common years while allowing for non-common years.
    # Using a full outer join and filling NaNs for plotting.
    combined_years_df = pd.merge(release_year_counts, year_added_counts, left_on='release_year', right_on='year_added', how='outer', suffixes=('_release', '_added'))
    combined_years_df.fillna(0, inplace=True)
    combined_years_df['year'] = combined_years_df['release_year'].fillna(combined_years_df['year_added']).astype(int)
    combined_years_df.sort_values(by='year', inplace=True)

    plt.figure(figsize=(15, 7))
    sns.lineplot(x='year', y='release_count', data=combined_years_df, label='Release Count', marker='o')
    sns.lineplot(x='year', y='added_count', data=combined_years_df, label='Added Count', marker='x')
    plt.title('Content Release Year vs. Content Added Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Titles')
    plt.legend()
    plt.grid(True)
    plt.savefig('release_vs_added_year.png')
    plt.close()
    print("Generated: release_vs_added_year.png")

except FileNotFoundError:
    print("Error: netflix_titles.csv not found. Make sure it's in the same directory as the script.")
except Exception as e:
    print(f"An error occurred: {e}") 