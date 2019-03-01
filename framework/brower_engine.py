import os.path
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger

logger=Logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):
    dir=os.path.dirname(os.path.abspath('.'))
    chrome_driver_path=dir+'/tools/chromedriver.exe'
    ie_driver_path=dir+'/tools/IEDriverServer.exe'
    geck_driver_path=dir+'/tools/geckdriver.exe'

    def open_browser(self):
        config=ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(file_path)

        brower=config.get("browserType","browerName")
        logger.info("You has select %s browser"%brower)
        url=config.get("testServer","URL")
        logger.info("The test server url is:%s"%url)

        if brower=="Firefox":
            self.driver=webdriver.Firefox(self.geck_driver_path)
            logger.info("Starting firefox brower")
        elif brower=="Chrome":
            self.driver=webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting chrome brower")
        elif brower == "Chrome":
            self.driver = webdriver.Chrome(self.ie_driver_path)
            logger.info("Starting IE brower")
        self.driver.get(url)
        logger.info("Open url:%s"%url)
        self.driver.maximize_window()
        logger.info("Maxizize the current window")
        self.driver.implicitly_wait(10)
        logger.info("Set impicitly wait 10 seconds")
    def quit_browser(self):
        logger.info("Now,Close and quit the browser")
        self.driver.quit()

