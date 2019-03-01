from framework.base import BasePage
from selenium.webdriver.common.by import By
import time

class Search(BasePage):
    search_name=(By.NAME,"srchtxt")
    search_submit=(By.NAME,"searchsubmit")
    search_click=(By.CSS_SELECTOR,".pbw a font")
    def content(self,text):
        time.sleep(3)
        self.sendkeys(text,*self.search_name)
        self.click(*self.search_submit)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.jihuo()
        self.click(*self.search_click)
        self.driver.switch_to.window(self.driver.window_handles[2])
        assert text in self.driver.title
