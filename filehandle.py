# Define a dictionary of liked songs
liked_songs = {
    "Bad Habits": "Ed Sheeran",
    "I'm Just Ken": "Ryan Gosling",
    "Mastermind": "Taylor Swift",
    "Uptown Funk": "Mark Ronson ft. Bruno Mars",
    "Ghost": "Justin Bieber"
}

# Function to display and write liked songs to a file
def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, "w") as file:
        file.write("Liked Songs:\n")
        for title, artist in liked_songs.items():
            file.write(f"{title} by {artist}\n")
    print(f"Your liked songs have been saved to {file_name}!")

# Call the function
write_liked_songs_to_file(liked_songs, "liked_songs.txt")
