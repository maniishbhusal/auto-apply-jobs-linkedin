import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")

chrome_driver_path = Service(
    "C:\Development\chromedriver_win32\chromedriver.exe")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=chrome_driver_path, options=chrome_options)

URL = "https://www.linkedin.com/"
driver.get(URL)
driver.maximize_window()

actions = ActionChains(driver)

# Login with Email and Password
email = driver.find_element(By.ID, "session_key")
password = driver.find_element(By.ID, "session_password")
time.sleep(5)
actions.click(email).send_keys(MY_EMAIL).click(
    password).send_keys(MY_PASSWORD).send_keys(Keys.ENTER).perform()
# skip_button = driver.find_element(By.XPATH, '//*[@id="ember26"]/button[2]')

# Searching Python
search_button = driver.find_element(
    By.XPATH, '//*[@id="global-nav-typeahead"]/input')
actions.click(search_button).send_keys(
    "Python").send_keys(Keys.ENTER).perform()

# Selecting Jobs, Experience Level and Remote Jobs Options
time.sleep(3)
jobs_button = driver.find_element(
    By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[1]/button')
actions.click(jobs_button).perform()

time.sleep(3)
all_filters_button = driver.find_element(
    By.XPATH, '//*[@id="search-reusables__filters-bar"]/div/div/button')
actions.click(all_filters_button).perform()

time.sleep(1)

entry_level_button = driver.find_element(By.ID, "advanced-filter-experience-2")
actions.click(entry_level_button).perform()
time.sleep(2)
remote_job_button = driver.find_element(
    By.ID, "advanced-filter-workplaceType-2")
# actions.click(remote_job_button).perform()
actions.click(remote_job_button).perform()
# time.sleep(7)
# driver.implicitly_wait(5)
show_results_button = driver.find_element(By.ID, "ember755")
actions.click(show_results_button).perform()
