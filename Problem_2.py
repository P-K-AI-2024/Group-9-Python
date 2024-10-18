def load_song_data(file_name):
    """Reads song data from a text file and stores it in a nested dictionary."""
    song_data = {}

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        for line in lines:
            #Each line splits by commas, and strips unnecessary whitespaces and quotes
            parts = [part.strip().strip('"') for part in line.split(",")]

            #Each line has that the correct format (5 parts: title, artist, album, genre, duration)
            if len(parts) != 5:
                print(f"Skipping invalid line: {line}")
                continue

            title, artist, album, genre, duration = parts

            # If the artist is not in the dictionary, start it with an empty list
            if artist not in song_data:
                song_data[artist] = []

            # Add the song information to the artist's list
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


def view_songs_database(song_data):
    """Displays all songs in the database."""
    if not song_data:
        print("No songs in the database.")
        return

    for artist, songs in song_data.items():
        print(f"\nSongs by {artist}:")
        for song in songs:
            print(f"  Title: {song['title']}, Album: {song['album']}, Genre: {song['genre']}, Duration: {song['duration']}")


def delete_song(song_data, artist, title):
    """Deletes a song by title from the database."""
    if artist in song_data:
        for song in song_data[artist]:
            if song['title'].lower() == title.lower():
                song_data[artist].remove(song)
                print(f"'{title}' by {artist} has been deleted.")
                if not song_data[artist]:  # Remove artist if no songs remain
                    del song_data[artist]
                return
    print(f"Error: Song '{title}' by {artist} not found.")


def modify_song_info(song_data, artist, title):
    """Modifies song information."""
    if artist in song_data:
        for song in song_data[artist]:
            if song['title'].lower() == title.lower():
                print(f"Current details for '{title}':")
                print(f"  Album: {song['album']}, Genre: {song['genre']}, Duration: {song['duration']}")

                #User Prompt for new details
                new_album = input("Enter new album (or press Enter to keep current): ")
                new_genre = input("Enter new genre (or press Enter to keep current): ")
                new_duration = input("Enter new duration (or press Enter to keep current): ")

                #Song Details Update if new input is provided
                if new_album:
                    song['album'] = new_album
                if new_genre:
                    song['genre'] = new_genre
                if new_duration:
                    song['duration'] = new_duration

                print(f"Updated details for '{title}':")
                print(f"  Album: {song['album']}, Genre: {song['genre']}, Duration: {song['duration']}")
                return
    print(f"Error: Song '{title}' by {artist} not found.")


def menu():
    """Displays the menu and handles user input."""
    song_data = {}

    while True:
        print("\n--- Songs Management System (Dev) ---")
        print("1. Load Song Data")
        print("2. View Songs Database")
        print("3. Delete a Particular Song")
        print("4. Modify Song Information")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            file_name = input("Enter the filename to load song data from (e.g., songs_data.txt): ")
            song_data = load_song_data(file_name)

        elif choice == '2':
            view_songs_database(song_data)

        elif choice == '3':
            artist = input("Enter the artist's name: ")
            title = input("Enter the title of the song to delete: ")
            delete_song(song_data, artist, title)

        elif choice == '4':
            artist = input("Enter the artist's name: ")
            title = input("Enter the title of the song to modify: ")
            modify_song_info(song_data, artist, title)

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


#Program Start
menu()
