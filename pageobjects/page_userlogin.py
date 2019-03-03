from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
import unittest

class UserLogin(BasePage):
    unit=unittest.TestCase()
    home_page_username_search_loc=(By.NAME,"username")
    home_page_pwd_search_loc = (By.NAME, "password")
    home_page_button_search_loc=(By.CSS_SELECTOR,".fastlg_l .pn")
    user_input=(By.CSS_SELECTOR,".vwmy a")
    def userlogin(self,name,pwd):
        self.sendkeys(name, *self.home_page_username_search_loc)
        self.sendkeys(pwd, *self.home_page_pwd_search_loc)
        self.click(*self.home_page_button_search_loc)

        actual_name = self.text(self.find_element(*self.user_input))
        print(actual_name)
        self.unit.assertEqual(actual_name, name, msg=actual_name)