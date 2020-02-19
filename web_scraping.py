from selenium import webdriver
import csv

with open("results.csv", "w") as f:
    f.write("Buyers, Price \n")

# Open up Chrome browser and navigate to webpage
browser = webdriver.Chrome()
browser.get("http://econpy.pythonanywhere.com/ex/001.html")

elems = browser.find_elements_by_xpath("//a[@href]")
sites = []
for elem in elems:
    sites.append((elem.get_attribute("href")))


for i in range(len(elems)):
    if i == 0:
        browser.get("http://econpy.pythonanywhere.com/ex/001.html")

        # Extract list of buyers and prices based on XPath
        buyers = browser.find_elements_by_xpath('//div[@title="buyer-name"]')
        prices = browser.find_elements_by_xpath('//span[@class="item-price"]')

        num_pages_items = len(buyers)
        with open("results.csv", "a") as f:
            for i in range(num_pages_items):
                f.write(f"{buyers[i].text} , {prices[i].text} \n")
    elif i == 1:
        for site in sites:
            browser.get(site)

            buyers = browser.find_elements_by_xpath('//div[@title="buyer-name"]')
            prices = browser.find_elements_by_xpath('//span[@class="item-price"]')

            num_pages_items = len(buyers)
            with open("results.csv", "a") as f:
                for i in range(num_pages_items):
                    f.write(f"{buyers[i].text} , {prices[i].text} \n")


# Close browser as cleanup
browser.close()
