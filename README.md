# Netflix Data Analysis Project

## Project Overview
This project provides a comprehensive data analysis of the Netflix dataset (`netflix_titles.csv`), focusing on understanding content trends, distributions, and key insights into Netflix's library. The analysis covers data cleaning, exploratory data analysis (EDA), and visualization to present findings effectively.

## Goals of the Project
- To clean and preprocess the raw Netflix dataset.
- To perform extensive Exploratory Data Analysis (EDA) to uncover patterns and trends.
- To visualize key aspects of the Netflix content using various charts and graphs.
- To derive actionable insights and conclusions from the data.

## Analysis Steps Performed

### 1. Data Collection & Cleaning
- Loaded the `netflix_titles.csv` dataset using pandas.
- Handled missing values in `director`, `cast`, and `country` columns by filling them with 'Unknown'.
- Dropped rows with missing `date_added` values.
- Imputed missing `rating` values with the most frequent rating.
- Processed the `duration` column to separate movie durations (in minutes) and TV show seasons, filling missing values with the mean for each type.
- Converted the `date_added` column to datetime objects for time-series analysis.

### 2. Exploratory Data Analysis (EDA) & Visualization
Various visualizations were generated to explore the dataset:
- **Content Type Distribution:** Bar chart showing the proportion of Movies vs. TV Shows.
- **Content Added Over Time:** Line plot illustrating the trend of content additions to Netflix annually.
- **Top Content-Producing Countries:** Bar chart displaying the top 10 countries contributing content.
- **Top Directors:** Bar chart highlighting the top 10 most prolific directors.
- **Top Actors:** Bar chart showcasing the top 10 actors appearing in the most titles.
- **Distribution of Content Ratings:** Bar chart showing the frequency of different content ratings.
- **Top Genres/Categories:** Bar chart of the top 10 most common genres/categories.
- **Content Release Year vs. Content Added Year:** Line plot comparing content release trends with content addition trends over time.

### 3. Key Insights and Conclusions
- Netflix's library is heavily skewed towards **Movies**.
- There has been a significant **increase in content additions** over the years.
- The **United States** is the dominant content producer.
- Specific directors and actors frequently contribute to the platform.
- The platform caters to a **diverse audience** with a range of content ratings and popular genres like Dramas, Comedies, and International Movies.
- Netflix actively adds both **newly released and older titles** to expand its catalog.

## Tools and Libraries Used
- **Python** (Programming Language)
- **pandas** (Data manipulation and analysis)
- **matplotlib** (Data visualization)
- **seaborn** (Statistical data visualization)

## How to Run the Analysis
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/UnnatiModanwal/netflix-data-analysis.git
    cd netflix-data-analysis
    ```
2.  **Install the required Python libraries:**
    ```bash
    pip install pandas matplotlib seaborn
    ```
3.  **Run the analysis script:**
    ```bash
    python netflix_analysis.py
    ```
    This will generate several `.png` image files in the project directory, representing the visualizations.

## Files in this Repository
- `netflix_titles.csv`: The raw dataset used for the analysis.
- `netflix_analysis.py`: The Python script containing the data cleaning, EDA, and visualization code.
- `content_type_distribution.png`: Visualization of content type distribution.
- `content_added_over_time.png`: Visualization of content added over time.
- `top_countries.png`: Visualization of top content-producing countries.
- `top_directors.png`: Visualization of top directors.
- `top_actors.png`: Visualization of top actors.
- `content_ratings_distribution.png`: Visualization of content ratings distribution.
- `top_genres.png`: Visualization of top genres/categories.
- `release_vs_added_year.png`: Visualization of release year vs. year added. 