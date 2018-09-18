# -*- coding: utf-8 -*-
"""
Created on 2018/05/14
@author: mopon
"""
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def broswer_chrome():
    return webdriver.Chrome()
    # return webdriver.PhantomJS(executable_path=r"D:\Python27\phantomjs-1.9.7-windows\phantomjs.exe")


def broswer_firefox():
    binary = FirefoxBinary("D:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
    return webdriver.Firefox(firefox_binary=binary)


def broswer_phantomjs():
    return webdriver.PhantomJS(executable_path=r"D:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe")