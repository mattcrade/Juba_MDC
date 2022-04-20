import pandas as pd
import os

dirname = os.path.dirname(__file__)

file_path = r"..\data\track.csv"
new_path = r"..\data\track_feat.csv"

file = os.path.join(dirname, file_path)
f = os.path.join(dirname, new_path)

df = pd.read_csv(file, sep='|')
df.drop(columns=['speechiness',
                 'instrumentalness',
                 'acousticness',
                 'duration_ms',
                 'liveness',
                 'loudness',
                 'time_signature',
                 'mode',
                 'type'], inplace=True)


def b_func(x):
    if 0 <= x <= 0.1:
        return 1
    elif 0.1 < x <= 0.2:
        return 2
    elif 0.2 < x <= 0.3:
        return 3
    elif 0.3 < x <= 0.4:
        return 4
    elif 0.4 < x <= 0.5:
        return 5
    elif 0.5 < x <= 0.6:
        return 6
    elif 0.6 < x <= 0.7:
        return 7
    elif 0.7 < x <= 0.8:
        return 8
    elif 0.8 < x <= 0.9:
        return 9
    elif 0.9 < x <= 1:
        return 10


def b_func2(x):
    if 40 <= x <= 57.5:
        return 1
    elif 57.5 < x <= 75:
        return 2
    elif 75 < x <= 92.5:
        return 3
    elif 92.5 < x <= 110:
        return 4
    elif 110 < x <= 127.5:
        return 5
    elif 127.5 < x <= 145:
        return 6
    elif 145 < x <= 162.5:
        return 7
    elif 162.5 < x <= 180:
        return 8
    elif 180 < x <= 197.5:
        return 9
    elif 197.5 < x <= 215:
        return 10


df['danceability'] = df['danceability'].apply(b_func)
df['energy'] = df['energy'].apply(b_func)
df['valence'] = df['valence'].apply(b_func)
df['tempo'] = df['tempo'].apply(b_func2)
df.drop_duplicates(inplace=True, ignore_index=True)
df = df.reset_index(drop=True)
df.to_csv(f, sep='|', index=False)
