import pafy
import ytdl
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os


'''
The current objectives:

- Try to set up Spotify creds

- Try to get youtube audio stream
'''


os.environ["SPOTIPY_CLIENT_ID"] = "7d2ccf1b94b040838e9b3042cd8cb30d"
os.environ["SPOTIPY_CLIENT_SECRET"] = "12bb377086b244f3a0c7204feab4f6d9"

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


