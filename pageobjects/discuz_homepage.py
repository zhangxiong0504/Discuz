from framework.base import BasePage
from selenium.webdriver.common.by import By
import time

#继承basepage类
class HomePage(BasePage):
    home_page_username_search_loc=(By.NAME,"username")
    home_page_pwd_search_loc = (By.NAME, "password")
    home_page_button_search_loc=(By.CSS_SELECTOR,".fastlg_l .pn")
    home_page_mrbutton_search_loc=(By.CSS_SELECTOR,".fl_tb tr td h2 a")
    home_page_post_search_loc=(By.XPATH,"//div[@id='pgt']/a")
    title = (By.NAME,"subject")
    iframe=(By.TAG_NAME,"iframe")
    text_input = (By.TAG_NAME,"body")
    post_table = (By.ID,"postsubmit")
    reply = (By.ID,"post_reply")
    area = (By.ID,"postmessage")
    reply_add =(By.ID,"postsubmit")
    logout = (By.LINK_TEXT,"退出")
    #输入搜索内容，并提交
    def search(self,name,pwd,title,text,reply_text):
        self.sendkeys(name,*self.home_page_username_search_loc)
        self.sendkeys(pwd, *self.home_page_pwd_search_loc)
        self.click(*self.home_page_button_search_loc)
        time.sleep(3)
        self.jihuo()
        self.click(*self.home_page_mrbutton_search_loc)
        time.sleep(3)
        self.jihuo()
        self.click(*self.home_page_post_search_loc)
        time.sleep(3)
        self.jihuo()
        self.sendkeys(title,*self.title)
        self.frame(*self.iframe)
        self.sendkeys(text,*self.text_input)
        self.jihuo()
        self.click(*self.post_table)
        time.sleep(3)
        self.jihuo()
        self.click(*self.reply)
        time.sleep(3)
        self.jihuo()
        self.sendkeys(reply_text,*self.area)
        time.sleep(3)
        self.jihuo()
        self.click(*self.reply_add)
        time.sleep(3)
        self.jihuo()
        self.click(*self.logout)


