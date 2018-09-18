# -*- coding: utf-8 -*-
"""
Created on 2018/05/14
@author: mopon
"""
import urllib2


# 获取http状态码，返回值为int型
def get_http_status(url):
    request = urllib2.urlopen(url)
    return request.getcode()
