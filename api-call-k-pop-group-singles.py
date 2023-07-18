import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import polars as pl

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

artist_df = pl.read_csv('spotify_k_pop_popularity.csv')
print(artist_df)

uri_list = []
for tuple in artist_df.rows():
    uri_list.append(tuple[3])


data = {"name": [], 
        "debut_date": []}

debut_df = pl.DataFrame(data, schema = {
    "name": str,
    "debut_date": str})

print(debut_df)

for i in uri_list:

    results = spotify.artist_albums(i, limit=50, offset=0, album_type='single')
    artist = spotify.artist(i)

    artist_name = (artist["name"])

    total = (results["total"])
    # print(total)

    results2 = spotify.artist_albums(i, offset=total-1)

    debut_date = (results2["items"][0]["release_date"])

    debut_data = {"name": artist_name,
                  "debut_date": debut_date}
    
    df = pl.DataFrame(debut_data)
    debut_df.extend(df)

print(debut_df)
path = "spotify_k_pop_debut.csv"
debut_df.write_csv(path, separator= ",")
