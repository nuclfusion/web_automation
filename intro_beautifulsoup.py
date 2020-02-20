from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

import csv

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

with open("products.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Brand", "Product_Name", "Shipping_Cost"])

    for container in containers:
        brand_name = container.find("div", "item-info").a.img["title"]
        product_name = container.find("a", {"class": "item-title"}).text
        # product_price =
        ship_price = container.find("li", {"class": "price-ship"}).text.strip()

        writer.writerow([brand_name, product_name, ship_price])

# print(containers[0].find("li", {"class": "price-current"}))
