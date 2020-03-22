# Import packages
from selenium import webdriver
import urllib.request as ul
import time
import datetime

# Assign variables
username = "username"
password = 'password'
bt_url = "bt_url"
chrome_path = "chromedriver_path"


# Checks if internet connected is working
def internet_connected():
    try:
        # Check stackoverflow url if connection works
        ul.urlopen('https://stackoverflow.com/', timeout=5)
        return True
    except ul.URLError as error:
        return False


# Logs in to bt wifi with given credentials
def login_bt(username, password, bt_url):
    driver = webdriver.Chrome(chrome_path)
    driver.get(bt_url)
    driver.find_element_by_css_selector('button.cookieUI__btn.blue').click()
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('loginbtn').click()
    time.sleep(1)
    driver.close()


# Infinite loop to check every minute if internet connection is available and log in to wifi if not
while True:
    if internet_connected() == False:
        login_bt(username, password, bt_url)
        print("Wifi reestablished", datetime.datetime.now())
    time.sleep(60)
