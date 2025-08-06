from bs4 import BeautifulSoup


with open("website.html") as file:
  contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# Find a specific string
heading = soup.find(name="h1", id="name")
print(heading)
