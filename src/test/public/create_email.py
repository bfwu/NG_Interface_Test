# -*- coding: utf-8 -*-
"""
Created on 2018/05/14

@author: mopon
"""
import random


def createemail():
    u"""创建邮箱"""
    mailcode = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ1234567890'
    front = ''
    for i in range(8):
        front += random.choice(mailcode)
    back = random.randint(100, 9999)
    return front+'@'+str(back)+".com"
