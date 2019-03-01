import unittest
import HTMLTestRunner
from testsuites.test_discuz_search import BaiduSearch1
from testsuites.test_discuz_search2 import BaiduSearch2
from testsuites.test_discuz_search3 import BaiduSearch3
from testsuites.test_discuz_search4 import BaiduSearch4
import os


report_path=os.path.dirname(os.path.abspath('.'))+'/test_report/'
if not os.path.exists(report_path):os.mkdir(report_path)

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(BaiduSearch1))
# suite.addTest(unittest.makeSuite(BaiduSearch2))
# suite.addTest(unittest.makeSuite(BaiduSearch3))
# suite.addTest(unittest.makeSuite(BaiduSearch4))
if __name__=="__main__":
    html_report = report_path + r"\result.html"  # r定义存放报告的路径
    fp = open(html_report, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="单元测试报告", description="用例执行情况")
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)