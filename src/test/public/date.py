# -*- coding:utf-8 -*-

import time


def datetime():
    now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
    return now


def date():
    now = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    return now


def datetimeall():
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    return now
