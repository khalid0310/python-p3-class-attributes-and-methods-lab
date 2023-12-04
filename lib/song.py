# lib/song.py

class Song:
    # Class attribute to keep track of the number of songs
    count = 0

    # Class attributes to keep track of genres, artists, genre counts, and artist counts
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the count of songs
        Song.add_song_to_count()

        # Add the genre to the genres list
        Song.add_to_genres(self.genre)

        # Add the artist to the artists list
        Song.add_to_artists(self.artist)

        # Update the genre count
        Song.add_to_genre_count(self.genre)

        # Update the artist count
        Song.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
