from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://youtube.com")

searchbox = browser.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys("Binging with Babish")

searchButton = browser.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()
