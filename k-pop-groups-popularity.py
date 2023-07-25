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

#Set the limit to the max according to Spotify API
limit = 50

#Create offset with list comprehension
# Set the starting value
start_value = 0

# Set the step value (in this case, 50)
step = 50

# Set the number of elements you want in the list
num_elements = 15

# Generate the list of integers using list comprehension
offset = [start_value + step * i for i in range(num_elements)]

# Print the list
print(offset)

index = (list(range(limit)))
print(index)



for num in offset:
    results = spotify.search(q='genre:k-pop', limit = limit, offset = num, type='artist')
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


bts = spotify.search(q='artist:bts', limit = 1, offset = 0, type='artist')
followers = bts['artists']['items'][0]['followers']['total']
name = bts['artists']['items'][0]['name']
popularity = bts['artists']['items'][0]['popularity']
artist_uri = bts['artists']['items'][0]['uri']

data = {"name": name, 
            "popularity": popularity, 
            "followers": followers,
            "artist_uri": artist_uri} 

df = pl.DataFrame(data)

full_table.extend(df)
    

# print(full_table)

path = "spotify_k_pop_popularity.csv"
full_table.write_csv(path, separator= ",")

path = "/Users/ischneid/Code Studio/K-Pop-Type-Tok/K_Pop_Type_Tok/spotify_k_pop_popularity.csv"
full_table.write_csv(path, separator= ",")

#artists = results['items']
#while results['next']:
#    results = spotify.next(results)

#for album in albums:
#    print(album['name'])