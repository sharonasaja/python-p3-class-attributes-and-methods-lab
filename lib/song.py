class Song:
    count=0

    def __init__ (self,name,artist,genre):
         self.name = name
         self.artist = artist
         self.genre = genre
         self.add_song_to_count() 

      
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

# Create a new song
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")

# Access the attributes of the song
print(ninety_nine_problems.name)   
print(ninety_nine_problems.artist)
print(ninety_nine_problems.genre)  

# Check the count of songs
print(Song.count) 

class Song:
    count = 0  
    genres = []  
    artists = []  
    genre_count = {}  
    artist_count = {}   

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()  
        self.add_to_genres()  
        self.add_to_artists()  
        self.add_to_genre_count()  
        self.add_to_artist_count()  
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1

# Create songs
Oceaneyes = Song("oceaneyes", "Billie", "Pop")
Gloria = Song("Gloria", "Smith", "Rock")
Humble = Song("Humble", "Kendrick", "Rap")
Happy = Song("Happy", "william", "Pop")
song5 = Song("Song 5", "Smith", "Genre 2")
song6 = Song("Song 6", "Artist 9", "Rock")

# accessing class attributes
print(Song.genres) 
print(Song.artists)  
print(Song.genre_count)  
print(Song.artist_count)  
print(Song.count)

