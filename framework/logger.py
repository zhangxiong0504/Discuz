import logging
import time
import os


class Logger(object):
    def __init__(self,logger):
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #创建一个handler，用于写入日志文件
        rq=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        # log_path=os.path.dirname(os.getcwd())+'/logs/'#项目根目录下/logs保存日志
        log_path=os.path.dirname(os.path.abspath('.'))+'/logs/'
        log_name=log_path+rq+'.log'

        fh=logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


        formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
    def getlog(self):
        return self.logger
