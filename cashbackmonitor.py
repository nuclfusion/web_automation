from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request

import csv

CASH_BACK_MONITOR = "https://www.cashbackmonitor.com/cashback-store/"


class CashBack(object):
    """ Define CashBack object with URL and perform bs4 cleanup to print out portal, link, and rate """

    def __init__(self, store):
        self.store = store

        self.url = f"{CASH_BACK_MONITOR}{store}"

        self.driver = webdriver.Chrome()
        self.delay = 3

    def load_cashbackmonitor(self):
        self.driver.get(self.url)
        wait = WebDriverWait(self.driver, self.delay)

    def browser_quit(self):
        self.driver.close()

    def extract_cashback(self):

        self.load_cashbackmonitor()

        portal_name_raw = self.driver.find_elements_by_xpath('//td[@class="l lo"]')
        portal_name = [portal.text for portal in portal_name_raw]

        url_list_raw = self.driver.find_elements_by_xpath('//td[@class="l lo"]//a')
        portal_url = [link.get_attribute("href") for link in url_list_raw]

        cashback_raw = self.driver.find_elements_by_xpath('//td[@class="l"]//a//span')
        portal_cashback = [cash.text for cash in cashback_raw]

        cashback = zip(portal_name, portal_url, portal_cashback)
        print(list(cashback))

        self.browser_quit()


adidas = CashBack("adidas").extract_cashback()

