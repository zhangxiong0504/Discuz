import unittest
import time
# from selenium import webdriver
from testsuites.base_testcase import BaseTestCase
# from pageobjects.discuz_homepage import HomePage
from pageobjects.page_manage_login import Login
from pageobjects.page_reply import Reply
from pageobjects.page_post import Post
from pageobjects.page_user_exit import Exit


class BaiduSearch1(BaseTestCase):
    def test_baidu_search(self):
        # self.driver.get("http://www.baidu.com")
        # input_text=self.driver.find_element_by_css_selector(".s_ipt")
        # input_text.send_keys("selenium")
        # time.sleep(3)
        # input_click=self.driver.find_element_by_id("su")
        # input_click.click()
        # assert "百度" in self.driver.title
        # home_page=HomePage(self.driver)
        # home_page.open_url("http://www.baidu.com")
        login=Login(self.driver)
        login.login('admin','zx980504')
        post=Post(self.driver)
        post.post('title','hello')
        reply=Reply(self.driver)
        reply.reply('hello')
        exit=Exit(self.driver)
        exit.exit()
if __name__=="__main__":
    unittest.main()
