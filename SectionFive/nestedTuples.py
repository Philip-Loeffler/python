albums = [("Welcome to my nightmare", "alice cooper", 1975),
          ("bad company", "bad company", 1974),
          ("nightflight", "budgie", 1981),
          ("more mayhem", "emilda may", 2011),
          ("ride the lignting", "metallica", 1986),
          ]
# album list contains 5 tuples
# and each has 3 items in it
print(len(albums))


for album in albums:
    print("album: {}, artist: {}, year: {}".format(
        album[0], album[1], album[2]))

# unpacking the tuple
for name, artist, year in albums:
    print("album: {}, artist: {}, year: {}".format(
        name, artist, year))

# most important thing it seems about tuples, is that
# they are immutable, so you cant add items to them
# so from an architecture stand point if we had a tuple of albums,
# and wanted to add songs, we could use a tuple for the list of songs,
# because the songs on an album wont change, and if they were to change,
# it would because its a different album, i.e. bonus tracks ect
