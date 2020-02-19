from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request


class CraigslistScraper(object):
    def __init__(self, location, postal, max_price, radius, query=""):
        self.location = location
        self.postal = postal
        self.max_price = max_price
        self.radius = radius
        self.query = query

        self.url = f"https://{location}.craigslist.org/search/sss?query={query}&postal={postal}&max_price={max_price}&search_distance={radius}"

        self.driver = webdriver.Chrome()
        self.delay = 3

    def load_craigslist_url(self):
        self.driver.get(self.url)
        try:
            wait = WebDriverWait(self.driver, self.delay)
            wait.until(EC.presence_of_element_located((By.ID, "searchform")))
            print("Page is ready")
        except TimeoutException:
            print("Page has timed out")

    def extract_post_info(self):
        post_title_list = [
            post.text.split("\n")[-1].split(" ", 2)[-1].split("$")[0].strip()
            for post in self.driver.find_elements_by_class_name("result-row")
        ]
        print(post_title_list)

    def extract_post_urls(self):
        html_page = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(html_page, "lxml")
        url_list = [
            link["href"] for link in soup.findAll("a", {"class": "result-title hdrlnk"})
        ]

    def browser_quit(self):
        self.driver.close()


tampa_bay = CraigslistScraper("tampa", 34684, 100, 25, "dewalt")
tampa_bay.load_craigslist_url()
tampa_bay.extract_post_info()
tampa_bay.extract_post_urls()
tampa_bay.browser_quit()
