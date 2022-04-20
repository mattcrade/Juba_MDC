import itertools
from numpy import sort
import pandas as pd
from IPython.display import display
import pyTigerGraph as tg
from pprint import pprint

host = "https://rassan1.i.tgcloud.io"
username = "tigergraph"
password = "tigergraph"
graphname = "SpotifyGraph"
user_list = ["1", "2", "3", "4"]
pair_l = itertools.combinations(user_list, 2)


def user_audio_feat():
    conn = tg.TigerGraphConnection(host=host,
                                   username=username,
                                   password=password,
                                   graphname=graphname)
    conn.apiToken = conn.getToken(conn.createSecret())
    parameters = {
                "inputUser1": "1",
                "inputUser2": "2",
                "inputUser3": "3",
                "inputUser4": "4",
            }

    query = conn.runInstalledQuery(queryName="AvgAudioFeatures",
                                   params=parameters)
    return query


def user_combinations():
    pair_l = itertools.combinations(user_audio_feat(), 2)
    pair_list = []
    for i in pair_l:
        pair_list.append(i)
    return pair_list


def get_audio_similarity(u1, u2):
    new_dict = {}
    new_dict["first_user"] = u1["User"]
    new_dict["second_user"] = u2["User"]
    new_dict["danceability"] = round(abs((u1["danceability"] - u2["danceability"]) / (u1["danceability"] + u2["danceability"])), 4)
    new_dict["key"] = round(abs((u1["key"] - u2["key"]) / (u1["key"] + u2["key"])), 4)
    new_dict["valence"] = round(abs((u1["valence"] - u2["valence"]) / (u1["valence"] + u2["valence"])), 4)
    new_dict["energy"] = round(abs((u1["energy"] - u2["energy"]) / (u1["energy"] + u2["energy"])), 4)
    new_dict["tempo"] = round(abs((u1["tempo"] - u2["tempo"]) / (u1["tempo"] + u2["tempo"])), 4)
    new_dict["avg_feat_dist"] = round(((new_dict["danceability"] + new_dict["key"]+new_dict["valence"]+new_dict["energy"]+new_dict["tempo"])/5), 4)
    return new_dict


def user_comparison():
    user_diff_list = []
    pair_l = user_combinations()
    for pair in pair_l:
        user_diff = get_audio_similarity(pair[0], pair[1])
        user_diff_list.append(user_diff)
    udif_df1 = pd.DataFrame(user_diff_list)
    udif_df2 = udif_df1[udif_df1.first_user != udif_df1.second_user]
    udif_df2["filter_col"] = udif_df2.reset_index()[["first_user", "second_user"]].values.tolist()
    udif_df2.reset_index(inplace=True)
    # sort and create tuple of filter col values.
    for i, row in enumerate(udif_df2["filter_col"]):
        x = tuple(sort(row))
        udif_df2["filter_col"][i] = x

    df3 = udif_df2.drop_duplicates(subset=["filter_col"])
    df3.reset_index(inplace=True)
    df3.drop(columns=["filter_col", "level_0", "index"], inplace=True)
    display(df3)
    return(df3)


if __name__ == "__main__":
    user_comparison()
