from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import re
import os


CLIENT_ID  = os.environb['CLIENT_ID']
CLIENT_SECRET = os.environb['CLIENT_SECRET']
REDIRECT_URL = 'http://example.com'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username='Gabriel', 
    )
)

user_id = sp.current_user()["id"]


date = input('Which year do you want yo travel to? type the date in this format YYYY-MM-DD ')

padrao = r"^\d{4}-\d{2}-\d{2}$"

if not re.fullmatch(padrao, date):
    raise Exception('Data não segue padrão adequado!')

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}",headers=header)

response.raise_for_status()

soup = BeautifulSoup(response.text,'html.parser')

songs_tags = soup.select('div.chart-results-list div.o-chart-results-list-row-container > ul > li:nth-child(4) > ul > li:nth-child(1) > h3')

songs_list = [item.get_text().strip() for item in songs_tags]

year = date[0:4]
song_uri_list = []
for song in songs_list: 
    try:
        song_json = sp.search(q=f'track: {songs_list[0]} year: {year}"', type='track',limit=1)
        song_uri = song_json['tracks']['items'][0]['uri']
        song_uri_list.append(song_uri)
    except: 
        continue
    
playlist_infos = sp.user_playlist_create(user=user_id,name=f"{date} Billboard 100123", public=False)

sp.user_playlist_add_tracks(user_id,playlist_infos['id'],song_uri_list)

print('Done!!')
