from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from framework.logger import  Logger
from selenium.webdriver.common.action_chains import ActionChains
import unittest
# from selenium.webdriver.common.action_chains import ActionChains

import time
import os.path

logger=Logger(logger="BasePage").getlog()
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver

    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    def open_url(self,url):
        self.driver.get(url)

    def quit_browser(self):
        self.driver.quit()

    def close(self):
        try:
            self.driver.close()
            logger.info("Closeing  on current page.")
        except Exception as e:
            logger.error("Failed to close with on current page")

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(ec.visibility_of_element_located(loc))
            logger.info("找到页面元素--%s", loc)
            return self.driver.find_element(*loc)
        except:
            logger.error("%s页面中找不到%s元素"%(self,loc))
            self.get_windows_img()

    def find_elements(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(ec.visibility_of_all_elements_located(loc))
            logger.info("找到页面元素--%s", loc)
            return self.driver.find_elements(*loc)
        except:
            logger.error("%s页面中找不到%s元素"%(self,loc))
            self.get_windows_img()


    def get_windows_img(self):
         file_path=os.path.dirname(os.path.abspath('.'))+'/screenshots/'
         rq=time.strftime('%Y%m%d%H%%M',time.localtime(time.time()))
         screen_name = file_path + rq +'.png'
         try:
             self.driver.get_screenshot_as_file(screen_name)
             logger.info("Had take screenshot and save to folder:/ screenshots")
         except Exception as e:
             self.get_windows_img()
             logger.error("Failed to take screenshot! %s"%e)

    def sendkeys(self,text,*loc):
        try:
            el=self.find_element(*loc)
            el.clear()
            el.send_keys(text)
            logger.info("输入的内容%s",text)
        except Exception as e:
            logger.error("Failed to type in input box with %s"%e)

    def clear(self,*loc):
        el=self.find_element(*loc)
        try:
            el.clear()
            logger.info("Clear test is input box before typeing")
        except Exception as e:
            logger.error("Failed to clear is input box with %s"%e)

    def click(self,*loc):
        el=self.find_element(*loc)
        try:
            el.click()
            logger.info("Success The element was click")
        except Exception as e:
            logger.error("Failed to click the element with %s"%e)

    def jihuo(self):
        try:
            self.driver.switch_to.window(self.driver.current_window_handle)
            logger.info("Success switch to window")
        except Exception as e:
            logger.error("Failed Switch to window%s "%e)
    def frame(self,*loc):
        try:
            el = self.find_element(*loc)
            self.driver.switch_to.frame(el)
            logger.info("Success into inframe")
        except Exception as e:
            logger.error("Failed into inframe%s"%e)

    # def assert_equal(self,text,except_value):
    #     unit=unittest.TestCase()
    #     try:
    #         unit.assertEqual(text,except_value.text,msg=text)
    #         logger.info("text is equal with except_value")
    #     except Exception as e:
    #         logger.error("text is not equal with except_value%s"%e)

    def float(self,*loc):
        el = self.find_element(*loc)
        try:
            ActionChains(self.driver).move_to_element(el).perform()
            logger.info("Success find float ")
        except Exception as e:
            logger.error("Falied not find float ")

    def text(self, content):
        el = content.text
        try:
            logger.info("找到的文本%s", el)
            return el
        except Exception as e:
            logger.error("No found text")









