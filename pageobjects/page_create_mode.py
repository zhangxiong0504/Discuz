from framework.base import BasePage
from selenium.webdriver.common.by import By
import time

class Create_Mode(BasePage):
    froum=(By.ID,"header_forum")
    add_mode=(By.CSS_SELECTOR,".addtr")
    mode_name=(By.NAME,"newforum[1][]")
    submit=(By.NAME,"editsubmit")
    iframe = (By.TAG_NAME, "iframe")
    back=(By.CSS_SELECTOR,"#pt div >a:nth-child(5)")
    def create_mode(self,name):
        self.jihuo()
        self.click(*self.froum)
        self.frame(*self.iframe)
        self.click(*self.add_mode)
        self.clear(*self.mode_name)
        self.sendkeys(name,*self.mode_name)
        self.click(*self.submit)
        self.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(3)
        self.click(*self.back)
        self.jihuo()
