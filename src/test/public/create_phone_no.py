# -*- coding: utf-8 -*-
"""
Created on 2018/05/14

@author: mopon
"""
import random


def createphoneno():
    fs = 1
    se = "34578"
    last = random.randint(111111111, 999999999)
    return str(fs)+random.choice(se)+str(last)
