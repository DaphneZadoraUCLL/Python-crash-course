def make_album(artist_name, album_title, number_of_tracks=None):
    album = {'artist': artist_name,
             'title': album_title,
             'tracks': number_of_tracks
             }
    return album


album1 = make_album('Adele', '25', '11')
album2 = make_album('Drake', 'Scorpion', number_of_tracks='16')
album3 = make_album('Beyoncé', 'Lemonade')

print(album1)
print(album2)
print(album3)
