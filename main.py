import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import polars as pl

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

data_full = {"name": [], "popularity": [], "followers": []} 

full_table = pl.DataFrame(data_full, schema={"name": str, "popularity": pl.Int64, "followers": pl.Int64})

print(full_table)

limit = 50
index = (list(range(limit)))

results = spotify.search(q='genre:k-pop', limit = limit, type='artist')

for i in index:
    followers = results['artists']['items'][i]['followers']['total']
    name = results['artists']['items'][i]['name']
    popularity = results['artists']['items'][i]['popularity']

    data = {"name": name, "popularity": popularity, "followers": followers} 
    df = pl.DataFrame(data)

    full_table.extend(df)

    

print(full_table)

path = "spotify_k_pop_popularity.csv"
full_table.write_csv(path, separator= ",")

#artists = results['items']
#while results['next']:
#    results = spotify.next(results)

#for album in albums:
#    print(album['name'])