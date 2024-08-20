import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
import time
from Connect import Connect


load_dotenv(verbose=True)

class Login(Connect):

    def find_login_link(self):
            xpath = '//*[@id="account"]/div/a'  # 로그인 xpath
            login_btn = Connect.driver.find_element(By.XPATH, xpath)
            login_btn.click() #다음 화면으로 넘어감

            # print(login_btn.get_attribute("href"))
            # return login_btn.get_attribute("href")


    def login(self, ID, PW):
        # URL = self.find_login_link()
        # Connect.driver.get(URL)
        # id_xpath = '//*[@id="input_item_id"]'
        # pw_xpath ='//*[@id="input_item_pw"]'
        id_xpath = '//*[@id="id"]'
        pw_xpath = '//*[@id="pw"]'
        id_box = Connect.driver.find_element(By.XPATH, id_xpath)
        id_box.send_keys(ID)
        time.sleep(4)
        pw_box = Connect.driver.find_element(By.XPATH, pw_xpath)
        pw_box.send_keys(PW)
        time.sleep(2)
        id_box.submit()
        pw_box.submit()





if __name__ == '__main__':
    ID = os.getenv('NAVER_ID')
    PW = os.getenv('NAVER_PW')
    l = Login()
    l.find_login_link()
    l.login(ID, PW)
