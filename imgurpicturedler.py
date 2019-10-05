"""
    ways to get objects.
    By ID                   driver.find_element_by_id
    By Class Name           driver.find_element_by_class_name
    By Tag Name             driver.find_element_by_tag_name
    By Name                 driver.find_element_by_name
    By Link Text            driver.find_element_by_link_text
    By Partial Link Text    driver.find_element_by_partial_link_text
    By CSS                  driver.find_element_by_css_selector
    By XPath                driver.find_element_by_xpath

"""


import time
from selenium import webdriver 
# import pandas as pd 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

# urllib will save and download our links we extract.
import urllib.request as req

# create file stuff
import os

# get incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("detach", True)

# house keeping stuff
url = 'https://www.imgur.com'
search_term = 'pepe'
file_dir = 'D:/Pictures/' + search_term


# create directory if not already there.
if not os.path.exists(file_dir):
    os.makedirs(file_dir)

""" you can paste path of webdriver here """    
# driver = webdriver.Chrome(<LOCATION OF WEBDRIVER>)  # Optional argument, if not specified will search path.
driver = webdriver.Chrome(chrome_options=chrome_options) # enables incognito
driver.set_window_size(1080,640)
wait = WebDriverWait(driver,20)
driver.get(url); # this grabs your url link!

# driver.execute_script("window.scrollTo(0, 200)") 

search = driver.find_element_by_class_name('Searchbar-textInput')
# search = driver.find_elements_by_class_name('Searchbar-textInput')
# search = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"Searchbar-textInput"))).click()

search.click()
search.send_keys(search_term)
search.submit()



# scroll down to load new results
scroll_page_num = 5
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
for i in range(scroll_page_num):
    # scroll action
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # wait
    time.sleep(3)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

time.sleep(3)

# parse images
img_arr = []
images = driver.find_elements_by_tag_name('img')
for image in images:
    img = image.get_attribute('src')
    img_arr.append(img)
    print(img)



# save images

for i in range(len(img_arr)):
    # urllib.urlretrieve(img_arr[i], (i + '_' + pepe + '.png'))
    print('saving:', i + 1)
    req.urlretrieve(img_arr[i], (file_dir + '/' + str(i) + '.png'))
    # filename = '../' + str(i) + '_' + search_term + '.png'
    # with req.urlopen(img_arr[i]) as img, open(fname, 'wb') as opfile:
    #     data = img.read()
    #     opfile.write(data)

driver.close()

# first_box = driver.find_elements_by_id('thumbnail')