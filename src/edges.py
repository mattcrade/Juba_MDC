import pandas as pd
import os

# Assign the directory we are working in
dirname = os.path.dirname(__file__)

# Define the filepaths
user_top_tracks_filepath = r'../data/user_top_tracks.csv'
user_top_artists_filepath = r'../data/user_top_artists.csv'
user_has_top_track_filepath = r'../data/user_has_top_songs.csv'
user_has_artist_filepath = r'../data/user_has_artist.csv'
artist_has_album_filepath = r"../data/artist_has_album.csv"
path_chart_track = r"..\data\chart_track.csv"
path_user_top_track = r"..\data\user_top_tracks.csv"
path_artist_has_track = r"..\data\artist_has_track.csv"
path_artist_has_genre = r"..\data\artist_has_genre.csv"
path_album_has_track = r"..\data\album_has_track.csv"
path_artist = r"..\data\artist.csv"

# Define the files
user_has_artist_file = os.path.join(dirname, user_has_artist_filepath)
user_top_artists_file = os.path.join(dirname, user_top_artists_filepath)
user_has_top_track_file = os.path.join(dirname, user_has_top_track_filepath)
user_top_tracks_file = os.path.join(dirname, user_top_tracks_filepath)
artist_has_album_file = os.path.join(dirname, artist_has_album_filepath)
file_chart_track = os.path.join(dirname, path_chart_track)
file_user_top_track = os.path.join(dirname, path_user_top_track)
file_artist_has_track = os.path.join(dirname, path_artist_has_track)
file_artist_has_genre = os.path.join(dirname, path_artist_has_genre)
file_album_has_track = os.path.join(dirname, path_album_has_track)
file_artist = os.path.join(dirname, path_artist)


def get_user_has_top_track_edge():
    df = pd.read_csv(user_top_tracks_file, delimiter='|')
    df2 = df[['user', 'track_uri', 'track_name']]
    df2.drop_duplicates(inplace=True)
    df2.to_csv(user_has_top_track_file, index=False, sep='|')


def get_user_has_artist_edge():
    df = pd.read_csv(user_top_artists_file, delimiter='|')
    df2 = pd.read_csv(user_top_tracks_file, delimiter='|')
    df3 = df[['user', 'artist_name', 'artist_uri']]
    df4 = df2[['user', 'artist_name', 'artist_uri']]
    df5 = pd.concat([df3, df4], axis=0)
    df5.drop_duplicates(inplace=True)
    df5.to_csv(user_has_artist_file, index=False, sep='|')


def artist_has_album():
    top_track_df = pd.read_csv(user_top_tracks_file, delimiter='|')
    artist_has_album_df = top_track_df[['artist_name',
                                        'artist_uri',
                                        'album_name',
                                        'album_uri']]
    artist_has_album_df = artist_has_album_df.drop_duplicates()
    artist_has_album_df.to_csv(artist_has_album_file, index=False, sep="|")


def artist_has_genre():
    genre = pd.read_csv(file_artist, sep='|')
    genre = genre.drop(columns=['user', 'artist_uri', 'total_followers'])
    genre['genres'] = genre['genres'].str.replace('[', '').str.replace(']', '').str.replace("'", '').str.split(',')
    genre = genre.explode('genres')
    genre['genres'] = genre['genres'].str.strip()
    genre.to_csv(file_artist_has_genre, index=False, sep='|')


def album_has_track():
    df = pd.read_csv(file_user_top_track, sep='|')
    df = df.drop(columns=['user', 'artist_uri', 'artist_name'])
    df.to_csv(file_album_has_track, index=False, sep='|')


def artist_has_track_init():
    df = pd.read_csv(file_chart_track, sep='|')
    df = df.drop(columns=['album_uri',
                          'album_name',
                          'popularity',
                          'danceability',
                          'energy',
                          'speechiness',
                          'instrumentalness',
                          'tempo',
                          'acousticness',
                          'duration_ms',
                          'key',
                          'liveness',
                          'loudness',
                          'mode',
                          'time_signature',
                          'valence'])
    df2 = pd.read_csv(file_user_top_track, sep='|')
    df2 = df2.drop(columns=['user', 'album_uri', 'album_name'])
    return df, df2


def artist_has_track():
    chart = artist_has_track_init()[0]
    user = artist_has_track_init()[1]
    csvs = [user, chart]
    df = pd.concat(csvs)
    df.to_csv(file_artist_has_track, index=False, sep='|')


if __name__ == '__main__':
    artist_has_album()
    album_has_track()
    artist_has_track()
