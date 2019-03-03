from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
import unittest

class Delete(BasePage):
    unit=unittest.TestCase()
    home_page_mrbutton_search_loc = (By.CSS_SELECTOR, ".fl_tb tr td h2 a")
    delete_name=(By.NAME,"moderate[]")
    delete_click=(By.XPATH,"//div[@id='mdly']/p/strong/a")
    delete_confirmation=(By.NAME,"modsubmit")
    choise=(By.CSS_SELECTOR,"#mdly h6 span")
    choise_reson=(By.CSS_SELECTOR,".tpclg h4 span")
    def delete(self):
        time.sleep(3)
        self.jihuo()
        self.click(*self.home_page_mrbutton_search_loc)
        self.click(*self.delete_name)
        self.jihuo()

        cs= str(self.text(self.find_element(*self.choise)))
        print(cs)
        self.unit.assertEqual(cs, '选中', msg=cs)

        self.click(*self.delete_click)

        cr = str(self.text(self.find_element(*self.choise_reson)))
        print(cr)
        self.unit.assertEqual(cr, '操作原因:', msg=cr)

        self.jihuo()
        self.click(*self.delete_confirmation)