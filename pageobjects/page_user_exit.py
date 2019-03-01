from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
class Exit(BasePage):
    logout = (By.LINK_TEXT, "退出")
    def exit(self):
        time.sleep(3)
        self.click(*self.logout)