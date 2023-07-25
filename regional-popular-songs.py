import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import polars as pl

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

#Initialize Data Table

data_full = {'title': [],
            'artist': [],
            'date': [],
            'market': [],
            'popularity': []} 

main_df = pl.DataFrame(
    data_full, schema={'title': str,
                'artist': str,
                'date': str,
                'market': str,
                'popularity': pl.Int64})

# print(full_table)

#Set the limit to the max according to Spotify API
limit = 50

index = list(range(limit))
print(index)

# Generate the list of markets
markets = ["US", "MX", "BR", "KR"]

# Process the playlists and extract track information
for market in markets:
    results = spotify.search(q = "genre:k-pop", type='track', limit = limit, offset = 0, market = market)
    for i in index:
        try:
            artist = results["tracks"]["items"][i]["artists"][0]["name"]
            date = results["tracks"]["items"][i]["album"]["release_date"]
            name = results["tracks"]["items"][i]["name"]
            artist_id = results["tracks"]["items"][i]["name"]
            aritst_results = spotify.search(q = f"{artist}", type='artist', limit = 1, offset = 0, market = market)
            popularity = aritst_results['artists']['items'][0]['popularity']
            # print(f'{artist} - {name} - {market}')
        except IndexError:
            pass
        data = {'title': name,
                'artist': artist,
                'date': date,
                'market': market,
                'popularity': popularity}
        df = pl.DataFrame(data)
        main_df.extend(df)

print(main_df)

main_df.write_csv('/Users/ischneid/K-pop-spotify/spotify_k_pop_regional_singles.csv', separator= ',')