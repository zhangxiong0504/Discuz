from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
import unittest

class Reply(BasePage):
    unit=unittest.TestCase()
    reply1 = (By.ID, "post_reply")
    area = (By.ID, "postmessage")
    reply_add = (By.ID, "postsubmit")
    reply_title=(By.CSS_SELECTOR,"#thread_subject")
    def reply(self,reply_text):

        time.sleep(3)
        self.jihuo()

        self.click(*self.reply1)
        time.sleep(3)
        self.jihuo()

        reply_add_name = str(self.text(self.find_element(*self.reply_add)))
        print(reply_add_name)
        self.unit.assertEqual( reply_add_name, "参与/回复主题",msg=reply_add_name)

        self.sendkeys(reply_text, *self.area)
        time.sleep(3)
        self.jihuo()
        self.click(*self.reply_add)
        time.sleep(3)
        self.jihuo()