from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
import unittest
class Into_Manage(BasePage):
    unit=unittest.TestCase()
    manage_center=(By.CSS_SELECTOR,"#um > p:nth-child(2) > a:nth-child(16)")
    pwd_agein=(By.NAME,"admin_password")
    submit=(By.NAME,"submit")
    # ACP=(By.CSS_SELECTOR,".login")
    def create(self,pwd):
        self.click(*self.manage_center)
        self.driver.switch_to.window(self.driver.window_handles[1])

        # acp_text = str(self.text(self.find_element(*self.ACP)))
        # print(acp_text)
        # self.unit.assertEqual(acp_text, "Discuz! Administrator's Control Panel", msg=acp_text)

        self.sendkeys(pwd,*self.pwd_agein)
        self.click(*self.submit)

