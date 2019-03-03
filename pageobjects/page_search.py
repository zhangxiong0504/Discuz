from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
import unittest

class Search(BasePage):
    unit=unittest.TestCase()
    search_name=(By.NAME,"srchtxt")
    search_submit=(By.NAME,"searchsubmit")
    search_click=(By.CSS_SELECTOR,".pbw a font")
    search_text=(By.CSS_SELECTOR,".xs3 strong font")
    actual_search_text=(By.CSS_SELECTOR,"#thread_subject")
    def content(self,text):
        time.sleep(3)
        self.sendkeys(text,*self.search_name)
        self.click(*self.search_submit)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.jihuo()
        time.sleep(5)

        st= str(self.text(self.find_element(*self.search_text)))
        print(st)
        self.unit.assertEqual(st,text, msg=st)

        self.click(*self.search_click)
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.jihuo()

        actual_text = str(self.text(self.find_element(*self.actual_search_text)))
        print(actual_text)
        self.unit.assertEqual(actual_text, text, msg=actual_text)


