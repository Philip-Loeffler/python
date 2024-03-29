
class Song:
    """class to represent a song

    Attributes:
     title: string, the title of the song
     artist: artist, an artist object representing the song creator
     duration: int, the duration of the song in seconds. may be zero
    """


def __init__(self, title, artist, duration=0):
    """ Song init method

    Args:
    title: string, initalizes the 'title' attribute
    artist: Artist, A artist object representing the song's creator
    duration: optional, int, inital value for the duration attribute
        will default to zero if not specified

    """

    self.title = title
    self.artist = artist
    self.duration = duration


class Album:
    """ class to represent an album, using it's track list

    attributes:
    album_name: string, the name of the album
    year: int, the years the album was released
    artitst: artist, the artist responsible for the album
        if not specified the artist will default to an artist with the name various artist
    tracks: list, of songs, a list of the songs on the the album

    methods:
    addsong: used to add a new song to the albums track list
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """ adds a song to the track list
        Args:
        song, song, a song to add
        position, optional int, if specified the song will be added to that position in the track list - inserting
        it between other song if necessary. otherwise, the song will be added to the end of the list
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """basic class to store artist details

      Attributes:
      name: string, the name of the artist
      albums: list of albums, A list of the albums by the artist
          the lsit includes only those albums in this collection, it
          is not an exhaustive list of the artists published albums

      methods:
      add_album: used to add a new album to the artists album list
      """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """ add a new album to the list. 
        Args:
            album(album): album object to add to the list.
            if the album is already present, make sure it isnt
            added again.
        """
        self.albums.append(album)


def find_object(field, object_list):
    """check the object list which is passed as a param, to see if an object with a 'name' attribute equal to 'field'
        exists, and return it if so """
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("album.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(
                line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}:".format(artist_field,
                                        album_field, year_field, song_field))
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                # we've just read details for a new artist
                # retrieve the artist object if there is one.
                # otherwise create a new aetrist object and add it to the artist list
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                # if new album is none, we then create an object of an album, and pass data to it
                new_album = Album(album_field, year_field, new_album)
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                # we've just read a new album for the current artist
                # retrieve the album object is there is one
                # otherwise create a new album object and store it in the artist's collection
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album - Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)

            # create a new song object and add it to the current albums collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

    return artist_list


def create_checkfile(artist_list):
    """ create a check file from the object data for comparion with the original file"""
    with open("checkFile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == '__main__':
    artists = load_data()
