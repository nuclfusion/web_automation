import requests
from bs4 import BeautifulSoup as soup


result = requests.get("https://www.google.com")

# print(result.status_code)

# print(result.headers)

src = result.content

src_soup = soup(src, "lxml")

# print(src_soup)

links = src_soup.find_all("a")
# print(links)
for link in links:
    if "About" in link.text:
        print(link)
        print(link.attrs["href"])

