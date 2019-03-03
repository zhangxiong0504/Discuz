from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
import unittest
class Exit(BasePage):
    logout = (By.LINK_TEXT, "退出")
    id_input_text=(By.CSS_SELECTOR,"#ls_fastloginfield_ctrl")
    unit=unittest.TestCase()
    def exit(self):
        time.sleep(3)
        self.click(*self.logout)

        id_input= self.text(self.find_element(*self.id_input_text))
        print(id_input)
        self.unit.assertEqual(id_input, "用户名", msg=id_input)