# -*- coding: utf-8 -*-
"""
Created on 2018/05/14

@author: mopon
"""
import random
import datetime
import re

key = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}

# 省份代码
provice = ('11', '12', '13', '14', '15', '21', '22', '23', '31', '32', '33',
           '34', '35', '36', '37', '41', '42', '43', '44', '45', '46', '50',
           '51', '52', '53', '54', '61', '62', '63', '64', '65', '66')

# 加权数
coe = {1: 7, 2: 9, 3: 10, 4: 5, 5: 8, 6: 4, 7: 2, 8: 1, 9: 6, 10: 3, 11: 7, 12: 9, 13: 10, 14: 5, 15: 8, 16: 4, 17: 2}


def create_identitycard():
    """身份证生成"""
    # 出生日期
    birthdate = (datetime.date.today() - datetime.timedelta(days=random.randint(7000, 25000)))
    # 拼接前17位数字
    ident = provice[random.randint(0, 31)] + '0101' + birthdate.strftime("%Y%m%d") + str(random.randint(100, 999))
    sum = 0
    # 计算求和
    for i in range(17):
        sum += int(ident[i:i + 1]) * int(coe[i + 1])

    # 求模后对应的18位
    mo = key[sum % 11]
    return ident + mo


def verify_identitycard(identitycard):
    Errors = ['验证通过!', '身份证号码位数不对!',
              '身份证号码出生日期超出范围或含有非法字符!', '身份证号码校验错误!', '身份证地区非法!']
    identitycard = str(identitycard)
    # 删除空
    identitycard.strip()
    # 序列化
    list_ident = list(identitycard)

    # 区域验证
    # if(not provice[(identitycard)[0:2]]):
    # print Errors[4]

    # 15位验证
    if len(identitycard) == 15:
        if ((int(identitycard[6:8]) + 1900) % 4 == 0 or (
                            (int(identitycard[6:8]) + 1900) % 100 == 0 and (int(identitycard[6:8]) + 1900) % 4 == 0)):
            # 测试出生日期的合法性
            ereg = re.compile(
                    '[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}$')
        else:
            # 测试出生日期的合法性
            ereg = re.compile(
                    '[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}$')
            if re.match(ereg, identitycard):
                print Errors[0]
            else:
                print Errors[2]

    # 18位身份号码检测
    elif len(identitycard) == 18:
        # 出生日期的合法性检查
        if int(identitycard[6:10]) % 4 == 0 or (
                            int(identitycard[6:10]) % 100 == 0 and int(identitycard[6:10]) % 4 == 0):
            ereg = re.compile(
                    '[1-9][0-9]{5}19[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')  # //闰年出生日期的合法性正则表达式
        else:
            ereg = re.compile(
                    '[1-9][0-9]{5}19[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$')  # //平年出生日期的合法性正则表达式
        # 测试出生日期的合法性
        if re.match(ereg, identitycard):
            # 计算校验位
            sum = 0
            for i in range(17):
                sum += int(identitycard[i:i + 1]) * int(coe[i + 1])
            mo = sum % 11
            m = key[mo]
            if list_ident[17] == m:
                print Errors[0]
            else:
                print Errors[3]
        else:
            print Errors[2]
    else:
        print Errors[1]
