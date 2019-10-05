"""
    Learning Python Selenium
    # PASTE CHROMEDRIVER 77 (or chrome VERSION) in PYTHON ENVIRONMENT
"""

"""
    ways to get objects.
    By ID                   driver.find_element_by_id
    By Class Name           driver.find_element_by_class_name
    By Tag Name             driver.find_elements_by_tag_name
    By Name                 driver.find_elements_by_name
    By Link Text            driver.find_elements_by_link_text
    By Partial Link Text    driver.find_element_by_partial_link_text
    By CSS                  driver.find_element_by_css_selector
    By XPath                driver.find_elements_by_xpath

"""

import time
from selenium import webdriver

# get incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")


""" you can paste path of webdriver here """
# driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver = webdriver.Chrome(chrome_options=chrome_options) # enables incognito

driver.get('http://www.google.com/');

# prints title of webpage?
# print(driver.title)

time.sleep(2) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(2) # Let the user actually see something!
driver.quit()