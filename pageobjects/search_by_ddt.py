from selenium import webdriver
import unittest
from ddt import data, ddt, unpack
import time
from framework.until import Until
import os

data_path = os.path.dirname(os.path.abspath('.')) + '/data/data.xlsx'
testdata = Until.read_excal(data_path, "Sheet1")

@ddt
class Search_by_ddt(unittest.TestCase):

    def setUp(self):
        dir = os.path.dirname(os.path.abspath('.'))
        chrome_driver_path = dir + '/tools/chromedriver.exe'
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(5)

    @data(*testdata)
    def test_search_by_ddt(self, data):
        search_string = data["content"]
        print("搜索内容->：%s",search_string)
        search_input = self.driver.find_element_by_id('kw')

        # 找到后，键入 java 并提交搜索
        search_input.send_keys(search_string)
        time.sleep(3)
        search_input.submit()

    def tearDown(self):
        """测试结束后的操作，这里基本上都是关闭浏览器"""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()