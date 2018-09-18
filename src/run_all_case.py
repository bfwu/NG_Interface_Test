# -*- coding: utf8 -*-
import unittest
import HTMLTestRunner
from src.test.public import alldir, date


filename = alldir.save_report_dir() + date.date()+'_testlog.log'
f = open(filename, 'a')
f.write("\n"+"*"*50+"开始执行"+"*"*50)
f.write("\n"+"开始打印本次运行全用例脚本的日志,开始时间："+date.datetimeall()+"\n\n")
f.close()

 # 指明要自动查找的py文件所在文件夹路径

def createSuite():  # 产生测试套件
	base_dir = alldir.get_src_dir()
	testunit = unittest.TestSuite()
	# 使用discover找出用例文件夹下test_case的所有用例
	discover = unittest.defaultTestLoader.discover(base_dir+'src\\test\\test_case\\', pattern="test_*.py", top_level_dir=None)  # 测试模块的顶层目录，即测试用例不是放在多级目录下，设置为none
	for suite in discover:  # 使用for循环出suite,再循环出case
		for case in suite:
			testunit.addTests(case)
	print testunit
	return testunit
alltestnames = createSuite()
# 生成日志
filename = alldir.save_report_dir()+date.datetime()+'_test.html'
fp = file(filename, "wb")

runner = HTMLTestRunner.HTMLTestRunner(
	stream=fp,
	title=u"NG接口自动化测试报告",
	description=u"用例执行情况"
)
# 执行用例
print(u"开始运行脚本")
runner.run(alltestnames)
print(u"脚本运行结束")

filename = alldir.save_report_dir() + date.date()+'_testlog.log'
f = open(filename, 'a')
f.write("\n"+"结束打印本次运行全用例脚本的日志，结束时间："+date.datetimeall()+"\n")
f.write(("*"*50+"执行结束"+"*"*50+"\n"))
f.close()
