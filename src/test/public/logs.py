# -*- coding: utf-8 -*-
"""
Created on 2018/05/14
@author: mopon
"""
from src.test.public import alldir
from src.test.public import date
import inspect


def error(string):
    filepath = inspect.stack()[1][1]
    lineno = inspect.stack()[1][2]
    filename = alldir.save_report_dir() + date.date()+'_testlog.log'
    f = open(filename, 'a')
    f.write("【ERROR】"+string+"|"+date.datetimeall()+"|"+filepath+"|line:["+str(lineno)+"]\n")
    f.close()
    # logger = logging.getLogger()
    # logger.setLevel(logging.ERROR)
    # # 创建文件的handler
    # f_handler = logging.FileHandler(filename)
    # f_handler.setLevel(logging.ERROR)
    # # 设置日志输出格式
    # fmt = logging.Formatter("【%(levelname)s】 %(message)s| %(asctime)s |"+filename1+"[line:"+str(lineno)+"]")
    # # 给handler绑定一个fomatter类
    # f_handler.setFormatter(fmt)
    # # 绑定一个handler
    # logger.addHandler(f_handler)
    #
    # #
    # # logging.basicConfig(level=logging.ERROR,
    # #                     format="【%(levelname)s】 %(message)s| %(asctime)s |"+filename+"[line:"+str(lineno)+"]",
    # #                     datefmt='%a, %d %b %Y %H:%M:%S',
    # #                     filename=alldir.save_report_dir() + date.date()+'_testlog.log',
    # #                     disable_existing_loggers=False,
    # #                     defaults=None
    # #                     )
    # logging.error(string)


def info(string):
    filepath = inspect.stack()[1][1]
    lineno = inspect.stack()[1][2]
    filename = alldir.save_report_dir() + date.date()+'_testlog.log'
    f = open(filename, 'a')
    f.write("【INFO】"+string+"|"+date.datetimeall()+"|"+filepath+"|line:["+str(lineno)+"]\n")
    f.close()
