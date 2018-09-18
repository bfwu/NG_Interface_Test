# -*- coding: utf-8 -*-
"""
Created on 2018/05/14

@author: mopon
"""
import os
import sys
from src.test.public.date import date
import mainsys


def get_img_dir():
    u"""获取到img路径"""
    # 获取当前路径
    path = mainsys.mainsyspath()
    # path = sys.path[0]
    # print(path)
    #
    # if os.path.isdir(path):
    #     curpath = path
    # elif os.path.isfile(path):
    #     curpath = os.path.dirname(path)
    # print(curpath)
    #
    # # 分割路径为字符串
    # pathindex = curpath.split("\\")
    # print(pathindex)
    # # 查找路径的关键字
    # findindex = pathindex.index("test-lamppa-edu")
    # # 组合工程根路径
    # path = ''
    # for i in range(findindex+1):
    #     path = path + pathindex[i]+'\\'
    # # 拼接img路径
    imgpath = path+"\\src\\test\\img\\"
    return imgpath


def get_src_dir():
    u"""
   获取到工程根目录
   """
    # 获取当前路径
    path = mainsys.mainsyspath()
    # path = sys.path[0]
    # if os.path.isdir(path):
    #     curpath = path
    # elif os.path.isfile(path):
    #     curpath = os.path.dirname(path)
    # # 分割路径为字符串
    # pathindex = curpath.split("\\")
    #
    # # 查找路径的关键字
    # findindex = pathindex.index("test-lamppa-edu")
    # # 组合工程根路径
    # path = ''
    # for i in range(findindex+1):
    # path += pathindex[i]+'\\'
    srcpath = path + "\\"
    return srcpath


def save_report_dir():
    u"""
    将logs文件夹创建在工程目录
    """
    # 获取当前路径
    path = mainsys.mainsyspath()
    # curpath = os.getcwd()
    # path = sys.path[0]
    # if os.path.isdir(path):
    #     curpath = path
    # elif os.path.isfile(path):
    #     curpath = os.path.dirname(path)
    # # 分割路径为字符串
    # pathindex = curpath.split("\\")
    # # 查找路径的关键字
    # findindex = pathindex.index("test-lamppa-edu")
    # # 组合工程根路径
    # path = ''
    # for i in range(findindex):
    #     path = path + pathindex[i]+'\\'
    path += "\\logs\\"
    if os.path.exists(path):
        return path
    else:
        os.mkdir(path)
        return path


def save_screenshot_dir():
    u"""
    将screenshot文件夹创建在工程目录
    """
    # 获取当前路径
    path1 = mainsys.mainsyspath()
    # curpath = os.getcwd()
    # path = sys.path[0]
    # if os.path.isdir(path):
    #     curpath = path
    # elif os.path.isfile(path):
    #     curpath = os.path.dirname(path)
    # # 分割路径为字符串
    # pathindex = curpath.split("\\")
    # # 查找路径的关键字
    # findindex = pathindex.index("test-lamppa-edu")
    # # 组合工程根路径
    # path = ''
    # for i in range(findindex):
    #     path = path + pathindex[i]+'\\'
    path1 += "\\screenshots\\"+str(date())+"\\"
    if os.path.exists(path1):
        return path1
    else:
        os.makedirs(path1)
        return path1


def createdir():
    u"""
    根目录创建文件夹
    """
    path = "D:\\autotest_lamppa\\"
    if os.path.exists(path):
        return path
    else:
        os.mkdir(path)
        return path

