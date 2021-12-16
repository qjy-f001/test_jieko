# 导包
import unittest
from tool.HTMLTestRunner import HTMLTestRunner
# from tool.HTMLTestReportCN import HTMLTestRunner

# 组装测试套件
suite = unittest.defaultTestLoader.discover("./")


unittest.TextTestRunner().run(suite)


# 使用文本执行测试套件
# with open("../report/report.txt", "w", encoding="utf-8") as f:
#     unittest.TextTestRunner(stream=f, verbosity=2).run(suite)

# 生成html报告
# with open("../report/report.html", "wb") as f:
#     HTMLTestRunner(stream=f, verbosity=2).run(suite)

