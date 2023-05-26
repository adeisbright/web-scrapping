import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())
results = soup.find(id="ResultsContainer")

anchors = soup.find_all("a")
for anchor in anchors:
    print(anchor.get("href"), anchor.string)
# print(anchors)
