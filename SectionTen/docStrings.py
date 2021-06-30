
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
