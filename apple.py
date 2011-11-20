from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox() # Get local session of firefox
browser.get("http://www.apple.com/retail/iphone/") # Load page
elem = browser.find_element_by_css("a.button.rounded") # Find the query box
elem.click()
time.sleep(5) # Let the page load, will be added to the API
browser.close()