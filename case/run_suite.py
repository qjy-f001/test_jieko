# 导包
import unittest
# from tool.HTMLTestRunner import HTMLTestRunner  # 英文
# from tool.HTMLTestReportCN import HTMLTestRunner  # 中文
from tool.HTMLTestRunnerCN import HTMLTestReportCN  # 中文
import time

# 生成测试套件
suite = unittest.defaultTestLoader.discover('./')

# 设置报告存放路径及文件名
now_time = time.strftime('%Y%m%d_%H%M%S')  # 获取时间戳, 防止报告重名被覆盖
report_name = '../report/report{}.html'.format(now_time)

# unittest.TextTestRunner().run(suite)

# 打开报告写入文件流
# 注意: wb 以二进制形式写入内容到文件
with open(report_name, 'wb') as f:
    # 初始化执行对象
    """
    可选参数含义
    verbosity: 控制台输出结果信息的模式.默认 1:简要模式, 可选 2:详细模式
    title:生成的报告文件的内容标题
    description:测试环境的描述信息
    tester:测试人员信息(中文模板专有)
    """
    # 英文模板
    # runner = HTMLTestRunner(stream=f,
    #                         verbosity=2,
    #                         title='Web 自动化测试报告',
    #                         description='系统:macOS 浏览器:谷歌 编程语言:Python')

    # 中文模板
    runner = HTMLTestReportCN(stream=f,
                              verbosity=2,
                              title='Web 自动化测试报告',
                              description='系统:macOS 浏览器:谷歌 编程语言:Python',
                              tester='QA')
    # 调用执行方法生成测试报告
    runner.run(suite)
