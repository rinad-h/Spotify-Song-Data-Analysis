# Spotify-Song-Data-Analysis
This project provides a simple analysis of song features from a Spotify dataset. Using Python, the program performs statistical analysis on song features such as beats per minute (BPM), danceability, energy, and more. It also allows for visual representation of data through scatter plots.

## Features

- **Song Statistics**: Calculate and display the highest, lowest, and average values for different song features like BPM, danceability, energy, and more.
- **Year Span Analysis**: Determine the span of years covered by the dataset and display the details of the oldest song.
- **Visualizations**: Create scatter plots comparing different song features, such as Danceability vs. BPM.

## Installation

1. Clone this repository or download the project files.
2. Make sure you have Python installed (version 3.x recommended).
3. Install the necessary dependencies by running the following command in your terminal:

    ```bash
    pip install numpy matplotlib
    ```

4. Download or prepare the `spotify_data.csv` file, which contains the song data, and make sure it's in the same directory as the project.

## Dataset Structure

The dataset is expected to have the following columns:

- `title`: The name of the song.
- `artist(s)`: The artist(s) of the song.
- `release`: The release year of the song.
- `num_of_streams`: The number of streams the song has.
- `bpm`: The beats per minute of the song.
- `key`: The musical key of the song.
- `mode`: The mode (major or minor) of the song.
- `danceability`: The danceability score of the song.
- `valence`: The emotional positivity of the song.
- `energy`: The energy score of the song.
- `acousticness`: The acoustic score of the song.
- `instrumentalness`: The instrumental score of the song.
- `liveness`: The liveness score of the song.
- `speechiness`: The speechiness score of the song.

## How to Run

1. Ensure you have the dataset (`spotify_data.csv`) in the same folder as the Python script.
2. Run the Python script in your terminal or IDE:

    ```bash
    python spotify_analysis.py
    ```

3. Follow the prompts to choose a feature to analyze. You can view the highest, lowest, and mean values of the selected feature, and also see the year span of the dataset and details of the oldest song.

4. The program will also display a scatter plot comparing Danceability vs. BPM.
