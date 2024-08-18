from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

class Connect :
    driver = webdriver.Chrome(options,service=Service(ChromeDriverManager().install()))

    URL = "https://www.naver.com"
    driver.get(url=URL)
    time.sleep(5)


