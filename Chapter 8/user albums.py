def make_album(artist_name, album_title, number_of_tracks=None):
    album = {'artist': artist_name,
             'title': album_title,
             'tracks': number_of_tracks
             }
    return album


while True:
    print(f"\nPlease enter the artist's name and album title: ")
    print("(Enter 'q' at any time to quit)")

    artist = input('Artist Name:   ')
    if artist.lower() == 'q':
        break
    title = input('Album title:   ')
    if title.lower() == 'q':
        break
    tracks = input('Number of tracks in this album (optional): ')
    if tracks.lower() == 'q':
        break

    if tracks == '':
        album = make_album(artist, title)
    else:
        album = make_album(artist, title, tracks)
    print(album)
