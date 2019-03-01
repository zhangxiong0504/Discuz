from selenium import webdriver
import unittest
from framework.brower_engine import BrowserEngine
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        # self.driver=webdriver.Chrome("../tools/chromedriver.exe")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(5)
        self.brower=BrowserEngine()
        self.brower.open_browser()
        self.driver=self.brower.driver
    def tearDown(self):
        self.brower.quit_browser()
