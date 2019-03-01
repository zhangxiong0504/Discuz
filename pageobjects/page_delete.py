from framework.base import BasePage
from selenium.webdriver.common.by import By
import time

class Delete(BasePage):
    home_page_mrbutton_search_loc = (By.CSS_SELECTOR, ".fl_tb tr td h2 a")
    delete_name=(By.NAME,"moderate[]")
    delete_click=(By.XPATH,"//div[@id='mdly']/p/strong/a")
    delete_confirmation=(By.NAME,"modsubmit")
    def delete(self):
        time.sleep(3)
        self.jihuo()
        self.click(*self.home_page_mrbutton_search_loc)
        self.click(*self.delete_name)
        self.jihuo()
        self.click(*self.delete_click)
        self.jihuo()
        self.click(*self.delete_confirmation)