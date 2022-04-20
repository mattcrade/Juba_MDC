import pandas as pd
import os

dirname = os.path.dirname(__file__)

f_path = r"..\data\user_followed_artists.csv"
f_df = pd.read_csv(os.path.join(dirname, f_path))

a_path = r"..\data\user_top_artists.csv"
a_df = pd.read_csv(os.path.join(dirname, a_path))

t_path = r"..\data\user_top_tracks.csv"
t_df = pd.read_csv(os.path.join(dirname, t_path))

a_df = pd.concat([a_df, f_df], axis=0)

a_df.drop_duplicates(inplace=True, ignore_index=True)

a_df.drop(columns='artist_url', inplace=True)
t_df.drop(columns='track_url', inplace=True)

a_df.replace('mac5088', '1', inplace=True)
a_df.replace('hanakotj', '2', inplace=True)
a_df.replace('silverfail', '3', inplace=True)
a_df.replace('rassan98', '4', inplace=True)

a_df.rename(columns={'username': 'user'}, inplace=True)

t_df.replace('mac5088', '1', inplace=True)
t_df.replace('hanakotj', '2', inplace=True)
t_df.replace('silverfail', '3', inplace=True)
t_df.replace('rassan98', '4', inplace=True)

t_df.rename(columns={'username': 'user'}, inplace=True)

artist_path = r"..\data\user_top_artists.csv"
a_df.to_csv(os.path.join(dirname, artist_path), sep='|', index=False)

track_path = r"..\data\user_top_tracks.csv"
t_df.to_csv(os.path.join(dirname, track_path), sep='|', index=False)
