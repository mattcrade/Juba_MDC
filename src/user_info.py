import pandas as pd
import os
import spotipy


client_id = 'ENTER CLIENT ID'
client_secret = 'ENTER CLIENT SECRET'
username = "example"
redirect_uri = f'https://open.spotify.com/user/{username}'
scope = ['user-follow-read', 'user-top-read']
token = spotipy.util.prompt_for_user_token(username, scope, client_id,
                                           client_secret, redirect_uri)
sp = spotipy.client.Spotify(auth=token)


def get_user_top_tracks():
    tt = sp.current_user_top_tracks(limit=50, time_range='medium_term')
    tt_dict = {}
    for i in tt['items']:
        tt_dict[i['id']] = {'username': username,
                            'track_uri': '',
                            'track_url': '',
                            'track_name': '',
                            'artist_uri': '',
                            'artist_name': '',
                            'album_uri': '',
                            'album_name': ''}
        try:
            tt_dict[i['id']]['track_uri'] = i['id']
            tt_dict[i['id']]['track_url'] = i['external_urls']['spotify']
            tt_dict[i['id']]['track_name'] = i['name']
            tt_dict[i['id']]['artist_uri'] = i['artists'][0]['id']
            tt_dict[i['id']]['artist_name'] = i['artists'][0]['name']
            tt_dict[i['id']]['album_uri'] = i['album']['id']
            tt_dict[i['id']]['album_name'] = i['album']['name']
        except KeyError:
            continue
    return tt_dict


def get_user_top_artists():
    ta = sp.current_user_top_artists(limit=50, time_range='medium_term')
    ta_dict = {}
    for i in ta['items']:
        ta_dict[i['id']] = {'username': username,
                            'artist_uri': '',
                            'artist_url': '',
                            'artist_name': '',
                            'total_followers': 0,
                            'genres': ''}
        try:
            ta_dict[i['id']]['artist_uri'] = i['id']
            ta_dict[i['id']]['artist_url'] = i['external_urls']['spotify']
            ta_dict[i['id']]['artist_name'] = i['name']
            ta_dict[i['id']]['total_followers'] = i['followers']['total']
            ta_dict[i['id']]['genres'] = i['genres']
        except KeyError:
            continue
    return ta_dict


def get_followed_artists():
    fa = sp.current_user_followed_artists(limit=50)
    fa_dict = {}
    for i in fa['artists']['items']:
        fa_dict[i['id']] = {'username': username,
                            'artist_uri': '',
                            'artist_url': '',
                            'artist_name': '',
                            'total_followers': 0,
                            'genres': ''}
        try:
            fa_dict[i['id']]['artist_uri'] = i['id']
            fa_dict[i['id']]['artist_url'] = i['external_urls']['spotify']
            fa_dict[i['id']]['artist_name'] = i['name']
            fa_dict[i['id']]['total_followers'] = i['followers']['total']
            fa_dict[i['id']]['genres'] = i['genres']
        except KeyError:
            continue
    return fa_dict


def create_csvs():
    dirname = os.path.dirname(__file__)

    tt_df = pd.DataFrame.from_dict(get_user_top_tracks(), orient='index')
    tt_df.reset_index(inplace=True, drop=True)
    tt_path = r"..\data\user_top_tracks.csv"
    tt_df.to_csv(os.path.join(dirname, tt_path), index=False)

    ta_df = pd.DataFrame.from_dict(get_user_top_artists(), orient='index')
    ta_df.reset_index(inplace=True, drop=True)
    ta_path = r"..\data\user_top_artists.csv"
    ta_df.to_csv(os.path.join(dirname, ta_path), index=False)

    fa_df = pd.DataFrame.from_dict(get_followed_artists(), orient='index')
    fa_df.reset_index(inplace=True, drop=True)
    fa_path = r"..\data\user_followed_artists.csv"
    fa_df.to_csv(os.path.join(dirname, fa_path), index=False)


def append_to_csvs():
    dirname = os.path.dirname(__file__)

    tt_df = pd.DataFrame.from_dict(get_user_top_tracks(), orient='index')
    tt_df.reset_index(inplace=True, drop=True)
    tt_path = r"..\data\user_top_tracks.csv"
    tt_df.to_csv(os.path.join(dirname, tt_path),
                 mode='a', index=False, header=False)

    ta_df = pd.DataFrame.from_dict(get_user_top_artists(), orient='index')
    ta_df.reset_index(inplace=True, drop=True)
    ta_path = r"..\data\user_top_artists.csv"
    ta_df.to_csv(os.path.join(dirname, ta_path),
                 mode='a', index=False, header=False)

    fa_df = pd.DataFrame.from_dict(get_followed_artists(), orient='index')
    fa_df.reset_index(inplace=True, drop=True)
    fa_path = r"..\data\user_followed_artists.csv"
    fa_df.to_csv(os.path.join(dirname, fa_path),
                 mode='a', index=False, header=False)


if __name__ == "__main__":
    append_to_csvs()
