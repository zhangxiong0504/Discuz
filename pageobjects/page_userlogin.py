from framework.base import BasePage
from selenium.webdriver.common.by import By
import time

class UserLogin(BasePage):
    home_page_username_search_loc=(By.NAME,"username")
    home_page_pwd_search_loc = (By.NAME, "password")
    home_page_button_search_loc=(By.CSS_SELECTOR,".fastlg_l .pn")
    def userlogin(self,name,pwd):
        self.sendkeys(name, *self.home_page_username_search_loc)
        self.sendkeys(pwd, *self.home_page_pwd_search_loc)
        self.click(*self.home_page_button_search_loc)