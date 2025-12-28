# Use beautiful soup to scrape the billboard top 100 for a given date
# Extract all song titles from the list
# Use the Spotify API to create a new playlist for that particular date
# Search Spotify for each of those songs and add them to a playlist
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

time_input = input("Enter the time you want to jump to in this format YYYY-MM-DD: ")

URL = "https://www.billboard.com/charts/hot-100/"+time_input

TEMP1 = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"
TEMP2 = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet"
TEMP3 = "c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"
TEMP4 = "c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet"
# These are classes scrapped from the billboard website

CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = "http://example.com"
SPOTIFY_URL = "https://api.spotify.com/v1"
USERNAME = ""

# ------------- SCRAPE BILLBOARD AND GET 2 LISTS OF SONGS AND CORRESPONDING ARTISTS -------------
response = requests.get(URL)
data = response.text
soup = BeautifulSoup(data, "html.parser")
songs = [item.getText().strip() for item in soup.find_all(name="h3", id="title-of-a-story", class_=TEMP1)]
first_song = soup.find(name="h3", id="title-of-a-story", class_=TEMP2).getText().strip()
songs.insert(0, first_song)
artists = [item.getText().strip() for item in soup.find_all(name="span", class_=TEMP3)]
first_artist = soup.find(name="span", class_=TEMP4).getText().strip()
artists.insert(0, first_artist)

# ------------- ACCESS SPOTIFY AND MAKE AUTH -------------
scope = "playlist-modify-private"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        cache_path="token.txt",
        scope=scope,
        show_dialog=True,
        username=USERNAME,
    )
)
user_id = sp.current_user()["id"]

# ------------- CREATE PLAYLIST -------------
playlist = sp.user_playlist_create(
    user=user_id,
    name="Top 100 Billboard songs",
    public=False,
    collaborative=False,
    description=f"Top 100 Billboard songs on {time_input}",
)
playlist_id = playlist["id"]

# ------------- SEARCH FOR SONGS -------------


class NoSongFound(Exception):
    pass


uris = []
for index in range(0, len(songs)):
    try:
        search = sp.search(
            q=f"track:{songs[index]} artist:{artists[index]}",
            limit=1,
            offset=0,
            market=None,
            type="track",
        )
        if search["tracks"]["total"] == 0:
            raise NoSongFound
    except NoSongFound:
        pass
    else:
        uri = str(search["tracks"]["items"][0]["id"])
        uris.append(uri)

# ------------- ADD SONGS -------------
sp.playlist_add_items(playlist_id=playlist_id, items=uris)

print(sp.playlist_items(
    playlist_id=playlist_id,
    additional_types="track",
))