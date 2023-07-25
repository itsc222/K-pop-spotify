import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import polars as pl

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

artist_df = pl.read_csv('spotify_k_pop_popularity.csv')
# print(artist_df)

main_df_data = {'release_date': [],
            'name': [],
            'artist': []}

main_df = pl.DataFrame(main_df_data, schema = {'release_date': str,
                                               'name': str,
                                               'artist': str})

uri_list = []
for tuple in artist_df.rows():
    uri_list.append(tuple[3][15:])

# print(uri_list)

for uri in uri_list:
    albums = (spotify.artist_albums(uri, album_type = 'single', limit=50, offset=0)["items"][0:3])
    for album in albums:
        release_date = (album['release_date'])
        name = (album['name'])
        artist = (album['artists'][0]['name'])
    
        data = {'release_date': release_date,
            'name': name,
            'artist': artist}
    
        df = pl.DataFrame(data, schema = {'release_date': str,
                                      'name': str,
                                      'artist': str})
    
        main_df.extend(df)

print(main_df)

path = "spotify_k_pop_new_releases.csv"
main_df.write_csv(path, separator= ",")

path = "/Users/ischneid/Code Studio/K-Pop-Type-Tok/K_Pop_Type_Tok/spotify_k_pop_new_releases.csv"
main_df.write_csv(path, separator= ",")