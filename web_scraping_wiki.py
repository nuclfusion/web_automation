from bs4 import BeautifulSoup as soup
import urllib.request
from urllib.request import Request, urlopen

# Define url to scrape

wiki_url = "https://en.wikipedia.org/wiki/Nuclear_fusion"
response_object = urllib.request.urlopen(wiki_url)

wiki_soup = soup(response_object, "html.parser")

# Find first instance of a tag
containers = wiki_soup.findAll("a", href=True)

# Loop for all instances of a tag
for container in containers[0:10]:
    link_url = container["href"]
    try:
        titles = container["title"]
    except:
        continue

tables = wiki_soup.find_all("tr", style="height:2em;")
print(tables[0].text)
