import pandas as pd
import os
import requests

dirname = os.path.dirname(__file__)

tracks_path = r"..\data\track.csv"
file_tracks = os.path.join(dirname, tracks_path)


# Function for access token
def access_token(client_id='ENTER CLIENT ID',
                 client_secret='ENTER CLIENT SECRET'):
    AUTH_URL = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(AUTH_URL, {
                                 'grant_type': 'client_credentials',
                                 'client_id': client_id,
                                 'client_secret': client_secret})
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    return access_token


def get_tracks_list():
    df = pd.read_csv(file_tracks, sep='|')
    s = set(df.track_uri)
    l = list(s)
    return l


def get_track_album():
    token = access_token()
    l = get_tracks_list()
    d = {}
    for i in l:
        s = requests.get('https://api.spotify.com/v1/' + 'tracks/' + i,
                         headers={'Authorization': f'Bearer {token}'})
        try:
            s = s.json()
        except:
            continue
        d[i] = {'album_uri': '',
                'album_name': ''
                }
        try:
            d[i]['album_uri'] = s['album']['id']
            d[i]['album_name'] = s['album']['name']
        except KeyError:
            continue
    album_path = r"..\data\album.csv"
    album_file = os.path.join(dirname, album_path)
    df = pd.DataFrame.from_dict(d, orient='index')
    df = df[df.album_uri != '']
    df.drop_duplicates(inplace=True, ignore_index=True)
    filtered_df = df.reset_index(drop=True)
    filtered_df.to_csv(album_file, sep='|', index=False)


if __name__ == "__main__":
    get_track_album()
