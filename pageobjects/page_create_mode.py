from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
import unittest

class Create_Mode(BasePage):
    unit = unittest.TestCase()
    froum=(By.ID,"header_forum")
    add_mode=(By.CSS_SELECTOR,".addtr")
    mode_name=(By.NAME,"newforum[1][]")
    submit=(By.NAME,"editsubmit")
    iframe = (By.TAG_NAME, "iframe")
    back=(By.CSS_SELECTOR,"#pt div >a:nth-child(5)")
    manage_name=(By.CSS_SELECTOR,"#frameuinfo em")
    mode_manage=(By.CSS_SELECTOR,".itemtitle h3")
    new_button_table = (By.CSS_SELECTOR, "#category_1 > table tbody > tr:nth-child(2) > td:nth-child(2) > h2 > a")
    def create_mode(self,name):
        actual_name = self.text(self.find_element(*self.manage_name))
        print(actual_name)
        self.unit.assertEqual('admin',actual_name , msg=actual_name)

        self.jihuo()
        self.click(*self.froum)
        self.frame(*self.iframe)

        mode_manage_text = self.text(self.find_element(*self.mode_manage))
        print(mode_manage_text)
        self.unit.assertEqual('版块管理', mode_manage_text, msg=mode_manage_text)

        self.click(*self.add_mode)
        self.clear(*self.mode_name)
        self.sendkeys(name,*self.mode_name)
        self.click(*self.submit)
        self.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(3)
        self.click(*self.back)

        mode_text= self.text(self.find_element(*self.new_button_table))
        print(mode_text)
        self.unit.assertEqual(name, mode_text, msg=mode_text)

        self.jihuo()
