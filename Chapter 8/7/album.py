def make_album(artist, album, num_tracks=0):
    music = {
        "artist" : artist,
        "album" : album
        }
    if num_tracks:
        music["num_tracks"] = num_tracks
    return music

m1 = make_album("Switchfoot", "Native Tongue")
m2 = make_album("Ariana Grande", "Thank U, Next")
m3 = make_album("Avril Lavigne", "Head Above Water")

print(m1)
print(m2)
print(m3)

m4 = make_album("Miley Cyrus", "She Is Coming", 5)

print(m4)
