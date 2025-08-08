# Create a .txt file with the top 100 movies
# Start from 1 and use the following website
# https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/
# Example: <h3 class="title">100) Stand By Me</h3>

from bs4 import BeautifulSoup
import requests
import unicodedata

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

def scrape_top_100(url):
  response = requests.get(url)
  response.raise_for_status()

  # Use .content instead of .text so BS can detect the correct encoding
  soup = BeautifulSoup(response.content, "html.parser")

  detected = getattr(soup, "original_encoding", None)
  if detected:
    print("Detected page encoding:", detected)

  titles = []
  for element in soup.select("h3.title"):
    raw_title = element.get_text(strip=True)
    cleaned = raw_title.split(") ", 1)[-1]
    cleaned = unicodedata.normalize("NFC", cleaned)
    titles.append(cleaned)

  return titles

def save_to_file(titles, filename="movies.txt"):
  with open(filename, "w", encoding="utf-8") as f:
    for i, title in enumerate(titles, start=1):
      f.write(f"{i}. {title}\n")

def main():
  titles = scrape_top_100(url)
  save_to_file(titles)
  print(f"Saved {len(titles)} movies to movies.txt")

if __name__ == "__main__":
  main()
