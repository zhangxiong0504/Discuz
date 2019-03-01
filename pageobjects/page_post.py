from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
import unittest

class Post(BasePage):
    unit=unittest.TestCase()
    home_page_mrbutton_search_loc = (By.CSS_SELECTOR, ".fl_tb tr td h2 a")
    home_page_post_search_loc = (By.XPATH, "//div[@id='pgt']/a")
    title = (By.NAME, "subject")
    iframe = (By.TAG_NAME, "iframe")
    text_input = (By.TAG_NAME, "body")
    post_table = (By.ID, "postsubmit")
    new_button_table=(By.CSS_SELECTOR,"#category_1 > table tbody > tr:nth-child(2) > td:nth-child(2) > h2 > a")
    vote_post_click=(By.CSS_SELECTOR,".poll a")
    vote_title=(By.ID,"subject")
    vote_content1=(By.CSS_SELECTOR,"#pollm_c_1 > p:nth-child(1) > input")
    vote_content2=(By.CSS_SELECTOR,"#pollm_c_1 > p:nth-child(2) > input")
    vote_content3=(By.CSS_SELECTOR,"#pollm_c_1 > p:nth-child(3) > input")
    vote_submit=(By.CSS_SELECTOR,"#pollsubmit")
    text_title=(By.CSS_SELECTOR,"#thread_subject")
    text_content=(By.CSS_SELECTOR,".pvt")
    text_percent=(By.CSS_SELECTOR,".pcht  tbody > tr > td:nth-child(2)")
    # vote_percent1 = (By.CSS_SELECTOR, ".pcht  tbody > tr:nth-child(2) > td:nth-child(2)")
    # vote_percent2 = (By.CSS_SELECTOR, ".pcht  tbody > tr:nth-child(4) > td:nth-child(2)")
    # vote_percent3 = (By.CSS_SELECTOR, ".pcht  tbody > tr:nth-child(6) > td:nth-child(2)")
    # text_content1=(By.CSS_SELECTOR,".pcht tbody > tr:nth-child(1) >td:nth-child(2)")
    # text_content2 = (By.CSS_SELECTOR, ".pcht tbody > tr:nth-child(3) >td:nth-child(2)")
    # text_content3 = (By.CSS_SELECTOR, ".pcht tbody > tr:nth-child(5) >td:nth-child(2)")
    chose=(By.CSS_SELECTOR,"#option_1")
    mr_name=(By.CSS_SELECTOR,".xs2 a")
    reply_title = (By.CSS_SELECTOR, "#thread_subject")
    def post(self,title,text):
        time.sleep(3)
        self.jihuo()
        self.click(*self.home_page_mrbutton_search_loc)
        time.sleep(3)
        self.jihuo()
        time.sleep(3)

        mr = str(self.text(self.find_element(*self.mr_name)))
        print(mr)
        self.unit.assertEqual(mr,'默认版块',msg=mr)

        self.click(*self.home_page_post_search_loc)
        time.sleep(3)
        self.jihuo()

        post_table_name =str(self.text(self.find_element(*self.post_table)))
        print(post_table_name)
        self.unit.assertEqual(post_table_name,'发表帖子',msg=post_table_name)

        self.sendkeys(title, *self.title)
        self.frame(*self.iframe)
        self.sendkeys(text, *self.text_input)
        self.jihuo()
        self.click(*self.post_table)

        reply_title_name = str(self.text(self.find_element(*self.reply_title)))
        print(reply_title_name)
        self.unit.assertEqual(reply_title_name,title, msg=reply_title_name)



    def new_post(self,title,text):
        time.sleep(3)
        self.jihuo()
        self.click(*self.new_button_table)
        # time.sleep(3)
        # self.jihuo()
        self.click(*self.home_page_post_search_loc)
        time.sleep(3)
        self.jihuo()
        self.sendkeys(title, *self.title)
        self.frame(*self.iframe)
        self.sendkeys(text, *self.text_input)
        self.jihuo()
        self.click(*self.post_table)
    def vote_post(self,title,content1,content2,content3):
        time.sleep(3)
        self.jihuo()
        self.click(*self.home_page_mrbutton_search_loc)
        self.float(*self.home_page_post_search_loc )
        self.click(*self.vote_post_click)
        self.jihuo()
        time.sleep(3)
        self.sendkeys(title,*self.vote_title)
        self.sendkeys(content1,*self.vote_content1)
        self.sendkeys(content2, *self.vote_content2)
        self.sendkeys(content3, *self.vote_content3)
        self.click(*self.post_table)
        self.jihuo()
        self.click(*self.chose)
        self.click(*self.vote_submit)
        text=self.find_elements(*self.text_content)
        precent=self.find_elements(*self.text_percent)
        print("投票主题",self.text(self.find_element(*self.text_title)))
        for i in range(0,len(text)):
        # for text,precent in zip(self.find_elements(*self.text_content),self.find_elements(*self.text_percent)):
            print("投票内容",self.text(text[i]),"百分比",self.text(precent[i*2+1]))
        # self.text(*self.text_content1)
        # self.text(*self.vote_percent1)
        # self.text(*self.text_content2)
        # self.text(*self.vote_percent2)
        # self.text(*self.text_content3)
        # self.text(*self.vote_percent3)





