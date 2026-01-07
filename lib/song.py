class Song:
    # 1. Define all class attributes at the top
    count = 0
    artists = []
    genres = []
    artist_count = {}
    genre_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # 2. Call class methods to update shared data
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
       cls.count += 1

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

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)

# 4. Instances
song1 = Song("Bohemian Rhapsody", "Queen", "Rock")
song2 = Song("Rolling in the Deep", "Adele", "Pop")
song3 = Song("Shape of You", "Ed Sheeran", "Pop")

# 5. Output
print(f"Total Song Count: {Song.count}")
print(f"Genre Histogram: {Song.genre_count}")