import pandas as pd
import os

dirname = os.path.dirname(__file__)

# node paths
path_users = r"..\data\users.csv"
path_user_top_tracks = r"..\data\user_top_tracks.csv"
path_user_top_tracks_AF = r"..\data\chart_track.csv"
path_track = r"..\data\track.csv"
path_user_top_artists = r"..\data\user_top_artists.csv"
path_chart_track = r"..\data\chart_track.csv"
path_artist = r"..\data\artist.csv"
path_genre = r"..\data\genre.csv"

# node files
file_users = os.path.join(dirname, path_users)
file_user_top_tracks = os.path.join(dirname, path_user_top_tracks)
file_user_top_tracks_AF = os.path.join(dirname, path_user_top_tracks_AF)
file_track = os.path.join(dirname, path_track)
file_user_top_artists = os.path.join(dirname, path_user_top_artists)
file_chart_track = os.path.join(dirname, path_chart_track)
file_artist = os.path.join(dirname, path_artist)
file_genre = os.path.join(dirname, path_genre)


def users_node():
    users_list = ["1", "2", "3", "4"]
    users_df = pd.DataFrame(users_list, columns=["users"])
    users_df.to_csv(file_users, index=False, sep="|")


def track_list():
    # extract top tracks uri for api input
    base_top_track_df = pd.read_csv(file_user_top_tracks, delimiter="|")
    top_track_series = base_top_track_df["track_uri"]
    # extract chart_tracks data for api imput
    chart_top_tracks_df = pd.read_csv(file_chart_track, delimiter="|")
    chart_top_tracks_series = chart_top_tracks_df["track_uri"]
    # merge lists
    total_tracks = pd.concat([top_track_series, chart_top_tracks_series])
    top_track_list = list(total_tracks)
    return top_track_list


def track_node():
    base_top_track_df = pd.read_csv(file_user_top_tracks, delimiter="|")
    top_track_named_df = base_top_track_df[["track_name", "track_uri"]]
    chart_top_track_df = pd.read_csv(file_chart_track, delimiter="|")
    chart_top_track_named_df = chart_top_track_df[["track_name", "track_uri"]]
    merged_df = pd.concat([top_track_named_df, chart_top_track_named_df])
    track_init = pd.read_csv(file_track)
    track = pd.merge(merged_df, track_init, on="track_uri")
    track.to_csv(file_track, index=False, sep="|")


def artist_node():
    top_art_df = pd.read_csv(file_user_top_artists, delimiter="|")
    top_tracks_df = pd.read_csv(file_user_top_tracks, delimiter="|")
    chart_track_df = pd.read_csv(file_chart_track, delimiter="|")

    filtered_art_df = top_art_df[["artist_name", "artist_uri"]]
    filtered_tracks_df = top_tracks_df[["artist_name", "artist_uri"]]
    filtered_chart_track_df = chart_track_df[["artist_name", "artist_uri"]]

    base_artist_df = pd.concat([filtered_art_df,
                                filtered_tracks_df,
                                filtered_chart_track_df])
    artist_df = base_artist_df.drop_duplicates()
    artist_df.to_csv(file_artist, index=False, sep="|")


def genre_node():
    genre = pd.read_csv(file_user_top_artists, sep='|')
    genre = genre.drop(columns=['username',
                                'artist_uri',
                                'artist_url',
                                'artist_name',
                                'total_followers'])
    genre = genre['genres'].str.replace('[', '').str.replace(']', '').str.replace("'", '').str.split(',')
    genre = genre.explode('genres')
    genre = pd.DataFrame(genre)
    genre = genre['genres'].str.strip()
    df = genre.drop_duplicates()
    df.to_csv(file_genre, index=False)


if __name__ == "__main__":
    users_node()
    track_list()
    artist_node()
    genre_node()
