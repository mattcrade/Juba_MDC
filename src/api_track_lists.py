import pandas as pd
import os

dirname = os.path.dirname(__file__)

top200_path = r"..\data\daily_top200.csv"
viral_path = r"..\data\daily_viral50.csv"
art_topsongs_path = r"../data/artist_topsongs.csv"

file_top200 = os.path.join(dirname, top200_path)
file_viral = os.path.join(dirname, viral_path)
file_art_topsong = os.path.join(dirname, art_topsongs_path)


def track_list_top200():
    df = pd.read_csv(file_top200)
    s = set(df.track_uri)
    top_200_list = list(s)
    return top_200_list


def track_list_viral50():
    df = pd.read_csv(file_viral)
    s = set(df.track_uri)
    viral_50_list = list(s)
    return viral_50_list


def artist_top_songs_list():
    df = pd.read_csv(file_art_topsong)
    df["track_uri"] = df["song_id"]
    df2 = df["track_uri"].to_frame()
    s = set(df2.track_uri)
    top_songs_list = list(s)
    return top_songs_list
