import pandas as pd
import os
import requests
from api_track_lists import artist_top_songs_list, track_list_top200, track_list_viral50
from nodes import track_list

dirname = os.path.dirname(__file__)
top200_file_path = r"../data/top200_audiofeatures.csv"
topsongs_filepath = r"../data/topsongs_audiofeatures.csv"
path_tracks_init = r"../data/track.csv"

file_art_top200 = os.path.join(dirname, top200_file_path)
file_art_topsongs = os.path.join(dirname, topsongs_filepath)
file_tracks_init = os.path.join(dirname, path_tracks_init)


# Function for access token
def access_token(client_id="781964010396468f8617e02fa2ae20d9",
                 client_secret="4588ee5a04524ef287795003a189c46d"):
    AUTH_URL = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(AUTH_URL, {
                                  'grant_type': 'client_credentials',
                                  'client_id': client_id,
                                  'client_secret': client_secret})
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    return access_token


# Function for audio features in a dictionary
def get_audio_features():
    track_uris = track_list()
    feature_dict = {}
    token = access_token()
    for t_uri in track_uris:
        feature_dict[t_uri] = {'track_uri': '',
                               'danceability': 0,
                               'energy': 0,
                               'speechiness': 0,
                               'instrumentalness': 0,
                               'tempo': 0,
                               'acousticness': 0,
                               'duration_ms': 0,
                               'key': 0,
                               'liveness': 0,
                               'loudness': 0,
                               'mode': 0,
                               'time_signature': 0,
                               'type': '',
                               'valence': 0}
        s = requests.get('https://api.spotify.com/v1/' + 'audio-features/' +
                         t_uri, headers={'Authorization': f'Bearer {token}'})
        s = s.json()
        try:
            feature_dict[t_uri]['track_uri'] = s['id']
            feature_dict[t_uri]['danceability'] = s['danceability']
            feature_dict[t_uri]['energy'] = s['energy']
            feature_dict[t_uri]['speechiness'] = s['speechiness']
            feature_dict[t_uri]['instrumentalness'] = s['instrumentalness']
            feature_dict[t_uri]['tempo'] = s['tempo']
            feature_dict[t_uri]['acousticness'] = s['acousticness']
            feature_dict[t_uri]['duration_ms'] = s['duration_ms']
            feature_dict[t_uri]['key'] = s['key']
            feature_dict[t_uri]['liveness'] = s['liveness']
            feature_dict[t_uri]['loudness'] = s['loudness']
            feature_dict[t_uri]['mode'] = s['mode']
            feature_dict[t_uri]['time_signature'] = s['time_signature']
            feature_dict[t_uri]['type'] = s['type']
            feature_dict[t_uri]['valence'] = s['valence']
        except KeyError:
            continue

    df_features = pd.DataFrame.from_dict(feature_dict, orient='index')
    df_features = df_features[df_features.track_uri != '']
    filtered_df = df_features.reset_index(drop=True)
    filtered_df.to_csv(file_tracks_init, index=False)


if __name__ == "__main__":
    get_audio_features()
