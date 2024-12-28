import numpy as np
import matplotlib.pyplot as plt

# Data import section (Do not modify)
column_names = ['title', 'artist(s)', 'release', 'num_of_streams', 'bpm', 'key', 'mode', 'danceability', 'valence', 'energy', 'acousticness', 'instrumentalness', 'liveness', 'speechiness']
data = np.genfromtxt('spotify_data.csv', delimiter=',', skip_header=True, dtype=str)

# Function to calculate and print feature stats
def feature_stats(input_value):
    """
    Calculate the highest, lowest, and mean value of a song feature.
    Prints the required information and returns the index location of the highest value.
    """
    column_data = np.array([float(row[input_value]) for row in data], dtype='float')
    highest_value_index = np.argmax(column_data)
    lowest_value_index = np.argmin(column_data)
    mean_value = np.mean(column_data)

    print(f"\nHighest {column_names[input_value]}: {data[highest_value_index][0]} ({column_data[highest_value_index]})")
    print(f"Lowest {column_names[input_value]}: {data[lowest_value_index][0]} ({column_data[lowest_value_index]})")
    print(f"Mean {column_names[input_value]}: {mean_value}")

    return highest_value_index

# Function to calculate the span of release years and print details of the oldest song
def age_stats():
    """
    Calculate the total span of release years and output the artist, key, and mode of the oldest song.
    """
    release_years = np.array([int(row[2]) for row in data], dtype='int')
    total_span = np.max(release_years) - np.min(release_years)

    oldest_song_index = np.argmin(release_years)
    oldest_song_info = data[oldest_song_index]

    print(f"\nTotal span of release years: {total_span}")
    print(f"Oldest song: {oldest_song_info[1]} - Key: {oldest_song_info[5]}, Mode: {oldest_song_info[6]}")

# Main function to handle user interaction
def main():
    print("ENDG 233 Spotify Statistics\n")
    print("Song analysis options: ")
    for menu, option in enumerate(column_names):
        print(menu, option)
    print("Choose -1 to end the program.")

    user_input = int(input('Please enter a song feature to analyze (or -1 to end): '))

    while user_input != -1:
        if user_input == 2:
            age_stats()
        elif user_input in [3, 4, 7, 8, 9, 10, 11, 12, 13]:
            highest_index = feature_stats(user_input)
            print(f"Highest {column_names[user_input]} song: {data[highest_index][0]}")
        else:
            print('You must enter a valid menu option.')

        user_input = int(input('Please enter a song feature to analyze (or -1 to end): '))

    print("Ending the program. Thank you!")

    # Danceability vs BPM plot
    danceability = np.array([float(row[7]) for row in data], dtype='float')
    bpm = np.array([float(row[4]) for row in data], dtype='float')

    plt.scatter(bpm, danceability, alpha=0.5)
    plt.title('Danceability vs. Beats per Minute')
    plt.xlabel('BPM')
    plt.ylabel('Danceability')
    plt.show()

# Run the program
if __name__ == '__main__':
    main()
