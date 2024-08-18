from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager




class Connect :
    driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
    URL = "https://www.naver.com"
    driver.get(URL)



