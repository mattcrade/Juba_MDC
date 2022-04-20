import pyTigerGraph as tg
import itertools
import pandas as pd
from IPython.display import display
import os

dirname = os.path.dirname(__file__)
users_path = r"../data/users.csv"
users_file = os.path.join(dirname, users_path)

host = "https://rassan1.i.tgcloud.io"
username = "tigergraph"
password = "ENTER PASSWORD"
graphname = "SpotifyGraph"
user_list = [1, 2, 3, 4]
pair_l = itertools.combinations(user_list, 2)


def user_path_data():
    conn = tg.TigerGraphConnection(host=host,
                                   username=username,
                                   password=password,
                                   graphname=graphname)
    conn.apiToken = conn.getToken(conn.createSecret())

    # queries = conn.getInstalledQueries(fmt="py")
    dict_list = []
    for pair in pair_l:
        user1 = pair[0]
        user2 = pair[1]
        parameters = {
            "inputUser": user1,
            "inputUser2": user2
        }
        query = conn.runInstalledQuery(queryName="path_data",
                                       params=parameters)
        query_dict = {"first_user": user1, "second_user": user2}
        query_dict.update(dict(query[0]))
        query_dict.update(dict(query[1]))
        query_dict.update(dict(query[2]))
        dict_list.append(query_dict)
    path_data_df = pd.DataFrame(dict_list)
    display(path_data_df)
    return path_data_df


if __name__ == "__main__":
    user_path_data()
