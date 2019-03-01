import unittest
import time
# from selenium import webdriver
from testsuites.base_testcase import BaseTestCase
from pageobjects.page_manage_login import Login
from pageobjects.page_user_exit import Exit
from pageobjects.page_search import Search



class BaiduSearch3(BaseTestCase):
    def test_discuz_search(self):
        # self.driver.get("http://www.baidu.com")
        # input_text=self.driver.find_element_by_css_selector(".s_ipt")
        # input_text.send_keys("selenium")
        # time.sleep(3)
        # input_click=self.driver.find_element_by_id("su")
        # input_click.click()
        # assert "百度" in self.driver.title
        # home_page=HomePage(self.driver)
        # home_page.open_url("http://www.baidu.com")
        login=Login(self.driver)
        login.login('admin','zx980504')

        search=Search(self.driver)
        search.content("haotest")

        exit=Exit(self.driver)
        exit.exit()
if __name__=="__main__":
    unittest.main()
