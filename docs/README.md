## Instructions

### Run order

1. api_input_data.py:
    - generates two csv's; user_top_artists and user_top_tracks
2. user_edit.py:
    - cleans/anonymises users 
3. nodes.py
4. edges.py
5. album.py 
    - generates the ablum node csv

6. audio_feat generates the audio featrues for the track.csv file
7. audio_feat_breakdown generates segments the audio feature values into categories

8. api_track_list generates uri lists which are input into the API functions.

## Problem Statement

Improving and expanding user interaction and connectivity on Spotify

## Project Overview

This project aims to provide a framework, built on TigerGraph, which Spotify can implement to improve the interaction between their customers by determining how similar a user’s music taste is to their friends/other users.

Potential features which Spotify could implement; user similarity scores, see common artists/genres between users, discord/subreddit style channels for people to share new music and interact, public user following recommendations. These features could be implemented by querying the network of users which has been built in TigerGraph.

In this project, example user network data has been extracted from Spotify using the Spotify API and loaded into a TigerGraph instance. To determine the similarity of user’s music a query can be run which calculates the number of shortest paths (either length 2 or 4) between users, where the greater the number of paths, the more similar their music taste. In addition to this, a user’s song attributes (e.g., danceability, tempo, valance etc.) can be aggregated in order to determine what “type” of music they listen to.

These features could then be used together in order to build out a network of users with a similar music taste to you and enable them to create music channels to enhance interaction.


