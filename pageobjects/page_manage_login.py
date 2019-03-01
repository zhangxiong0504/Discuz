from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
import unittest

class Login(BasePage):
    home_page_username_search_loc=(By.NAME,"username")
    home_page_pwd_search_loc = (By.NAME, "password")
    home_page_button_search_loc=(By.CSS_SELECTOR,".fastlg_l .pn")
    actual=(By.CSS_SELECTOR,".vwmy")
    unit = unittest.TestCase()
    def login(self,name,pwd):
        self.sendkeys(name, *self.home_page_username_search_loc)
        self.sendkeys(pwd, *self.home_page_pwd_search_loc)
        self.click(*self.home_page_button_search_loc)
        time.sleep(3)

        actual_name=self.text(self.find_element(*self.actual))
        print(actual_name)
        self.unit.assertEqual(actual_name,name,msg=actual_name)