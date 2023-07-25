import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import polars as pl

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

data_full = {"name": [], 
             "popularity": [], 
             "followers": [], 
             "artist_uri": []} 

full_table = pl.DataFrame(
    data_full, schema={"name": str, 
                       "popularity": pl.Int64, 
                       "followers": pl.Int64,
                       "artist_uri": str})

print(full_table)

limit = 50
index = (list(range(limit)))

results = spotify.search(q='genre:k-pop', limit = limit, type='artist')

for i in index:
    for genre in results['artists']['items'][i]['genres']:
        if genre == 'k-pop girl group':
            followers = results['artists']['items'][i]['followers']['total']
            name = results['artists']['items'][i]['name']
            popularity = results['artists']['items'][i]['popularity']
            artist_uri = results['artists']['items'][i]['uri']

            data = {"name": name, 
            "popularity": popularity, 
            "followers": followers,
            "artist_uri": artist_uri} 
            df = pl.DataFrame(data)

            full_table.extend(df)
        if genre == 'k-pop boy group':
            followers = results['artists']['items'][i]['followers']['total']
            name = results['artists']['items'][i]['name']
            popularity = results['artists']['items'][i]['popularity']
            artist_uri = results['artists']['items'][i]['uri']

            data = {"name": name, 
            "popularity": popularity, 
            "followers": followers,
            "artist_uri": artist_uri} 
            df = pl.DataFrame(data)

            full_table.extend(df)

    

print(full_table)

path = "spotify_k_pop_popularity(top50).csv"
full_table.write_csv(path, separator= ",")

path = "/Users/ischneid/Code Studio/K-Pop-Type-Tok/K_Pop_Type_Tok/spotify_k_pop_popularity(top50).csv"
full_table.write_csv(path, separator= ",")

#artists = results['items']
#while results['next']:
#    results = spotify.next(results)

#for album in albums:
#    print(album['name'])