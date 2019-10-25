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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# import pandas as pd 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

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
file_dir = './Pictures/' + search_term

"""
    FILL IN YOUR USERNAME AND PASSWORD FOR IMGUR. YOU CANNOT SEARCH WITHOUT IT!
"""
my_username = ''
my_pw = ''


# create directory if not already there.
if not os.path.exists(file_dir):
    os.makedirs(file_dir)


"""
    ===========SELECT YOUR DRIVER===========
    if you have a docker image and ready, just paste it below for the first driver. 
    Otherwise, use local webdriver and comment out the first driver.
"""
driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
# driver = webdriver.Chrome(chrome_options=chrome_options) # enables incognito

driver.set_window_size(1080,640)
# wait = WebDriverWait(driver,20)
driver.get(url); # this grabs your url link!

# driver.execute_script("window.scrollTo(0, 200)") 


# Need to sign in for imgur now for some reason... =/
signin = driver.find_element_by_class_name('Navbar-signin')
signin.click()

time.sleep(1)

# delete before PUSH!!!!

username = driver.find_element_by_name('username')
username.click()
username.send_keys(my_username)
pw = driver.find_element_by_name('password')
pw.click()
pw.send_keys(my_pw)
submit = driver.find_element_by_name('submit')
submit.click()

time.sleep(5)

search = driver.find_element_by_class_name('Searchbar-textInput')
search.click()
search.send_keys(search_term)
time.sleep(1)
search.submit()

time.sleep(1)

# for some reason we have to do this again because it loads weird things?
search = driver.find_element_by_class_name('logo-icon')
search.click()
search = driver.find_element_by_class_name('Searchbar-textInput')
search.click()
search.send_keys(search_term)
time.sleep(1)
search.submit()

# load first image
search = driver.find_element_by_xpath("//div[@id='4PfOUt7']//img")
search.click()

# save link from image.
img_arr = []

# images = driver.find_elements_by_tag_name("img")
num_of_images = 20

for i in range(num_of_images):

    time.sleep(2)

    # collect all images
    # images = driver.find_elements_by_tag_name('img')
    # videos = driver.find_elements_by_tag_name('source')

    
    # check if page is images, gifs or videos.
    images = driver.find_elements_by_xpath("//div[@class='image post-image']//img")
    videos = driver.find_elements_by_xpath("//div[@class='image post-image']//video")
    sources = driver.find_elements_by_xpath("//div[@class='image post-image']//source")

    # images
    for image in images:
        item = image.get_attribute('src')
        if 'imgur' not in str(item):
            print('not an imgur image')
            continue
        if item in img_arr:
            continue
        img_arr.append(item)
        print(item)
    
    # videos
    for video in videos:
        item = video.get_attribute('src')
        if 'imgur' not in str(item):
            print('not an imgur video')
            continue
        if item in img_arr:
            continue
        img_arr.append(item)
        print(item)

    # sources
    for source in sources:
        item = source.get_attribute('src')
        if 'imgur' not in str(item):
            print('not an imgur video')
            continue
        if item in img_arr:
            continue
        img_arr.append(item)
        print(item)

    # get image by clicking next post
    next_post = driver.find_element_by_class_name('navNext')
    next_post.click()

for img in img_arr:
    print(img)

# save images
for i in range(len(img_arr)):
    # urllib.urlretrieve(img_arr[i], (i + '_' + pepe + '.png'))
    print('saving:', i + 1)
    file_extension = img_arr[i].split('.')
    if file_extension[-1] == 'mp4':
        req.urlretrieve(img_arr[i], (file_dir + '/' + str(i) + '.mp4'))
    elif file_extension[-1] == 'gif':
        req.urlretrieve(img_arr[i], (file_dir + '/' + str(i) + '.gif'))
    else:
        req.urlretrieve(img_arr[i], (file_dir + '/' + str(i) + '.png'))

# driver.close()