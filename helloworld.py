"""
    Learning Python Selenium
    # PASTE CHROMEDRIVER 77 (or chrome VERSION) in PYTHON ENVIRONMENT
"""

import time
from selenium import webdriver



driver = webdriver.Chrome(""" you can paste path of webdriver here """)  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');

print(driver.title)

time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()