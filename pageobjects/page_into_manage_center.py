from framework.base import BasePage
from selenium.webdriver.common.by import By
import time

class Into_Manage(BasePage):
    manage_center=(By.CSS_SELECTOR,"#um > p:nth-child(2) > a:nth-child(16)")
    pwd_agein=(By.NAME,"admin_password")
    submit=(By.NAME,"submit")
    def create(self,pwd):
        self.click(*self.manage_center)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.sendkeys(pwd,*self.pwd_agein)
        self.click(*self.submit)

