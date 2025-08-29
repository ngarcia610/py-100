# Use beautiful soup to scrape the billboard top 100 for a given date
# Extract all song titles from the list
# Use the Spotify API to create a new playlist for that particular date
# Search Spotify for each of those songs and add them to a playlist

from bs4 import BeautifulSoup
import requests

date = input("Please enter the date. YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"}

response = requests.get(url=URL, headers=header)

soup = BeautifulSoup(response.text, "html.parser")
container = soup.select(".o-chart-results-list-row-container")

songs_list = [item.find(name="h3", id="title-of-a-story").getText().strip() for item in container]
artists_list = [item.find(name="h3", id="title-of-a-story").parent.span.getText().strip() for item in container]

print(songs_list)
print(artists_list)