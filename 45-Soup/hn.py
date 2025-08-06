# Pulls articles from Hacker News
# Populates lists for titles, links, and upvotes
# Finds the most upvoted post, and prints the title and link

from bs4 import BeautifulSoup
import requests

ARTICLE_LINKS = []
ARTICLE_TEXT = []
ARTICLE_SCORE = []

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")
news = soup.find_all(class_="titleline")
scores = soup.find_all(class_="score")

# Gather links and headline text
for heading in news:
    ARTICLE_LINKS.append(heading.find(name="a").get("href"))
    ARTICLE_TEXT.append(heading.find(name="a").getText())

# Gather scores
for score in scores:
    ARTICLE_SCORE.append(int(score.getText().split(" ")[0]))

# Find the highest scored article and print the headline, link, and score
max_value = max(ARTICLE_SCORE)
max_index = ARTICLE_SCORE.index(max_value)

print(f"The highest score was: {max_value}")
print(f"The headline was: {ARTICLE_TEXT[max_index]}")
print(f"The link to the article is: {ARTICLE_LINKS[max_index]}")
