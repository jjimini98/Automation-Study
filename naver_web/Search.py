from selenium.webdriver.common.by import By
from Connect import Connect

class Search(Connect):

    def search_item(self,key):
        xpath = '//*[@id="query"]' #검색창 xpath
        search_box = Connect.driver.find_element(By.XPATH, xpath)
        search_box.send_keys(key)
        search_box.submit()
        print(f"'{key}' 검색 완료")

if __name__ == '__main__':
    s = Search()
    s.search_item("최정훈")