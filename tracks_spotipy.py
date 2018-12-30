import spotipy
import os
import json
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyClientCredentials
import subprocess

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

userid = 'uwgt2xm7ki3gpeknlzdm9vpbg'

#userid: uwgt2xm7ki3gpeknlzdm9vpbg?si=HiRiBAcBQXSzrfnwmSx-vg
#userid = 'uwgt2xm7ki3gpeknlzdm9vpbg?si=dyua8wNrQ3GXEeDdlGt7ww'
#user id = uwgt2xm7ki3gpeknlzdm9vpbg
# https://open.spotify.com/user/uwgt2xm7ki3gpeknlzdm9vpbg?si=65LbDz5GRKK-Nh2E9lPdMQ


os.chdir('/mnt/c/Users/andre/Music')
music = os.listdir(os.getcwd())
idx = music.index('Unknown Music')
music.pop(idx)
idx2 = music.index('.cache-uwgt2xm7ki3gpeknlzdm9vpbg')
music.pop(idx2)

#print (music)

#scope = 'playlist-modify-public'
try:
    token = util.prompt_for_user_token(userid, 'playlist-modify-private')
except:
    os.remove(f".cache-{userid}")
    token = util.prompt_for_user_token(userid, 'playlist-modify-private')

#Create spotify Object
sp = spotipy.Spotify(auth = token)

sp.user_playlist_create(userid, 'Old Music', public = False)

music_uri = []
for i in range(0, len(music)):
    results = sp.search(music[i], type = 'album', limit = 1)
    #print (type(results))
    album_uri = results["albums"]["items"][0]["uri"]

    #print (json.loads(results, sort_keys = True, indent = 4))
    #print (album_uri)
    album_uri_app = album_uri[14:len(album_uri)]
    music_uri.append(album_uri_app)

    #for i in range(len(music)):
    #    search_query = sp.search(music[i], limit = 1, offset = 0, type = 'album')
        

    #print(json.dumps(user, sort_keys = True, indent = 4))

#print (music_uri)

tracks_uri = []

for i in range(0, len(music_uri)):
    tracks = sp.album_tracks(music_uri[i], limit = None, offset = 0)
    for j in range(0, len(tracks['items'])):
        tracks_uri_app = tracks['items'][j]['uri']
        tracks_uri_app = tracks_uri_app[14:len(tracks_uri_app)]
        tracks_uri.append(tracks_uri_app)

#1L5IleffQJk0fxiszsy2mA
#sp.user_playlist_add_tracks(userid, '1L5IleffQJk0fxiszsy2mA', tracks_uri[0:100], position = None)
#print ('done1')
#sp.user_playlist_add_tracks(userid, '1L5IleffQJk0fxiszsy2mA', tracks_uri[100:200], position = None)
#print ('done2')
#sp.user_playlist_add_tracks(userid, '1L5IleffQJk0fxiszsy2mA', tracks_uri[200:300], position = None)
#print ('done3')
sp.user_playlist_add_tracks(userid, '1L5IleffQJk0fxiszsy2mA', tracks_uri[300:len(tracks_uri)], position = None)
print('done4')