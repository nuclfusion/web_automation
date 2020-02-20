from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# URL for site to be scraped
my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"

# Opens connection to website
uClient = uReq(my_url)
page_html = uClient.read()

# Closes connection to website
uClient.close()

# Sort out raw html data
page_soup = soup(page_html, "html.parser")

# Grabs each product
containers = page_soup.findAll("div", {"class": "item-container"})
container = containers[0]
print(container.find("div", "item-info").a.img["title"])
