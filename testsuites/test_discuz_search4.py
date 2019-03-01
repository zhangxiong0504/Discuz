import unittest
import time
# from selenium import webdriver
from testsuites.base_testcase import BaseTestCase
from pageobjects.page_manage_login import Login
from pageobjects.page_user_exit import Exit
from pageobjects.page_post import Post
from framework.logger import Logger


logger=Logger(logger="BaiduSearch4").getlog()

class BaiduSearch4(BaseTestCase):
    def test_discuz_search(self):

        login=Login(self.driver)
        login.login('admin','zx980504')

        post_vote=Post(self.driver)
        post_vote.vote_post("最喜欢吃什么？","苹果","香蕉","橘子")

        exit=Exit(self.driver)
        exit.exit()
if __name__=="__main__":
    unittest.main()
