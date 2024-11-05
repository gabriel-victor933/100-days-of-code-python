import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID  = 'ef8bef6181aa4b3c93a0311e63fe426c'
CLIENT_SECRET = '65c83379236c46c39395dd3b28f2f11a'
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