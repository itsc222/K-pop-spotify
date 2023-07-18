import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import polars as pl

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

limit = 10

print(list(range(limit)))

results = spotify.search(q='genre:k-pop', limit = limit, type='artist')

followers = results['artists']['items'][0]['followers']['total']
name = results['artists']['items'][0]['name']
popularity = results['artists']['items'][0]['popularity']

print(tuple(name, popularity, followers))



#artists = results['items']
#while results['next']:
#    results = spotify.next(results)

#for album in albums:
#    print(album['name'])