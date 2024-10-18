def load_song_data(file_name):
    """Reads song data from a text file and stores it in a nested dictionary."""
    song_data = {}

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        for line in lines:
            #Each line splits by commas and strips unnecessary whitespaces and quotes
            parts = [part.strip().strip('"') for part in line.split(",")]

            #Each line has the correct format (5 parts: title, artist, album, genre, duration)
            if len(parts) != 5:
                print(f"Skipping invalid line: {line}")
                continue

            title, artist, album, genre, duration = parts

            # If the artist is not in the dictionary, create an empty list
            if artist not in song_data:
                song_data[artist] = []

            #add the song information to the artist's list
            song_data[artist].append({
                'title': title,
                'album': album,
                'genre': genre,
                'duration': duration
            })

        print(f"Successfully loaded song data from '{file_name}'.")

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return song_data


def search_song_by_title(song_data, title):
    """Searches for a song by title (case-insensitive) and displays its details."""
    title = title.strip().lower()  #we can search title by any means, here it has made it case-insensitive
    found = False

    for artist, songs in song_data.items():
        for song in songs:
            if song['title'].strip().lower() == title:
                print(f"\nSong found: '{song['title']}' by {artist}")
                print(f"  Album: {song['album']}, Genre: {song['genre']}, Duration: {song['duration']}")
                found = True

    if not found:
        print(f"Error: The song titled '{title}' does not exist in the database.")


def search_songs_by_artist(song_data, artist):
    """Searches for all songs by a specific artist (case-insensitive) and displays their details."""
    artist = artist.strip().lower()  #same as the artist name for case-insensitive search
    found = False

    for artist_key, songs in song_data.items():
        if artist_key.strip().lower() == artist:
            print(f"\nSongs by {artist_key}:")
            for song in songs:
                print(f"  Title: {song['title']}, Album: {song['album']}, Genre: {song['genre']}, Duration: {song['duration']}")
            found = True

    if not found:
        print(f"Error: No songs found for the artist '{artist}'.")


def menu():
    """Displays the menu and handles user input."""
    song_data = load_song_data("songs_data.txt")  #songs data loaded from file on start

    while True:
        print("\n--- Songs Management System (User) ---")
        print("1. Search for a Song by Title")
        print("2. Search for All Songs by an Artist")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            title = input("Enter the title of the song: ")
            search_song_by_title(song_data, title)

        elif choice == '2':
            artist = input("Enter the artist's name: ")
            search_songs_by_artist(song_data, artist)

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


#main menu
menu()
