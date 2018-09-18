# -*- coding: utf-8 -*-
"""
Created on 2018-07-16
@author: lenovo
"""
import re
from src.test.public.date import datetimeall
import datetime


def tag1(test):
    tg1 = "<" + test + ">" + "[\s\S]*?" + "</" + test + ">"
    return tg1


def tag2(test):
    tg2 = "<" + test + ">"
    return tg2


def tag3(test):
    tg3 = "</" + test + ">"
    return tg3


# 获取节点的属性值
def get_value(name, xml):
    text = re.findall(tag1(name), xml)
    value_list = []
    for te in text:
        testare = re.sub(tag2(name), "", te)
        value = re.sub(tag3(name), "", testare)
        value_list.append(value)
        # print("%s=" % name + value)
    return value_list


# 获取影厅返回影厅值
def get_screen_code(msg):
    cdata = re.findall(r'ScreenCode=.[0-9]{16}', msg)
    value_list = []
    for session in cdata:
        cdata = re.sub("ScreenCode=.", "", session)
        value_list.append(cdata)
    return value_list


# 匹配网络用户，替换网络用户
def replace_username(username, msg):
    macth_data = re.findall("Username=.[A-Za-z0-9]*", msg)
    for name in macth_data:
        macth_data = re.sub("Username=.", "", name)
    msg = msg.replace(macth_data, username)
    return msg


# 获取订单返回订单值
def get_order_code(msg):
    cdata = re.findall(r'OrderCode=.[0-9]{16}', msg)
    value_list = []
    for session in cdata:
        cdata = re.sub("OrderCode=.", "", session)
        value_list.append(cdata)
    return value_list


# 获取返回状态 status
def get_keyOfValue(key, msg):
    # cdata = re.findall(r'Status="[\s\S]*>', msg)
    # cdata = re.search(r'%s="([^"^>]+)' % (key), msg).group(1)
    pre = re.search(r'%s="([^"^>]+)' % (key), msg)
    if pre is None:
        return "NULL"
    return pre.group(1)


# 修改节点的属性值
def replace_data(name, olddata, newdata, xml):
    repstr = (tag2(name) + "{}" + tag3(name)).format(olddata)
    strinfo = re.compile(repstr)
    xml = strinfo.sub((tag2(name) + "{}" + tag3(name)).format(newdata), xml)
    return xml


# 匹配日期替换日期
def replace_date(today, msg):
    match_date = re.compile(r"(\d{4}-\d{1,2}-\d{1,2})")
    msg = re.sub(match_date, today, msg)

    return msg


# 匹配影院替换影院
def replace_cinema(cinema_code, msg):
    cdata = re.findall(r'CinemaCode=.[0-9]{8}', msg)
    for cinema in cdata:
        cdata = re.sub("CinemaCode=.", "", cinema)
    msg = msg.replace(cdata, cinema_code)
    return msg


# 匹配影院放映计划替换放映计划
def replace_session_code(session_code, msg):
    cdata = re.findall(r'SessionCode=.[0-9]{16}', msg)
    for session in cdata:
        cdata = re.sub("SessionCode=.", "", session)
    msg = msg.replace(cdata, session_code)
    return msg


# 匹配影厅替换影厅
def replace_screen_code(screen_code, msg):
    cdata = re.findall(r'ScreenCode=.[0-9]{16}', msg)
    for session in cdata:
        cdata = re.sub("ScreenCode=.", "", session)
    msg = msg.replace(cdata, screen_code)
    return msg


# 匹配座位替换座位
def replace_seat_code(seat_code, msg):
    cdata = re.findall(r'SeatCode=.[0-9]{16}', msg)
    for session in cdata:
        cdata = re.sub("SeatCode=.", "", session)
    msg = msg.replace(cdata, seat_code)
    return msg


# 匹配订单号替换订单号
def replace_order_code(order_code, msg):
    cdata = re.findall(r'OrderCode=.[0-9]{16}', msg)
    for session in cdata:
        cdata = re.sub("OrderCode=.", "", session)
    msg = msg.replace(cdata, order_code)
    return msg


# msg = '<Seat Price="35.02" SeatCode="0300000700200101"/>'
# 匹配成交价格替换价格
def replace_price(price, msg):
    cdata = re.findall(r'Price=.[\d+\.\d]*', msg)
    for session in cdata:
        cdata = re.sub("Price=.", "", session)
    msg = msg.replace(cdata, price)
    return msg


# 获取返回状态 status
def get_status(msg):
    # cdata = re.findall(r'Status="[\s\S]*>', msg)
    cdata = re.search(r'Status="([^"^>]+)', msg).group(1)
    return cdata


# 返回ErrorCode
# msg = """"><SubmitO39" ErrorCode="1" ErrorMessage="地面结算价低于影片的最低价,最低价:30.0,渠道价:7.0" Id="ID_Se"></"""
def get_error_code(msg):
    cdata = re.findall(r'ErrorCode="[\d]{0,3}', msg)
    for session in cdata:
        cdata = re.sub("ErrorCode=.", "", session)
    # cdata = re.search(r'ErrorCode="([^"^>]+)', msg).group(1)
    return cdata


# 获取错误提示
# msg = """"><SubmitO39" ErrorMessage="地面结算价低于影片的最低价,最低价:30.0,渠道价:7.0" Id="ID_Se"></"""
def get_error_message(msg):
    # cdata = re.findall(r'Status="[\s\S]*>', msg)
    cdata = re.search(r'ErrorMessage="([^"^>]+)', msg).group(1)
    return cdata


# 获取时间
# msg = """<StartTime>2018-07-19T08:45:00</StartTime><StartTime>2018-07-19T18:45:00</StartTime>  """
def get_time(msg):
    # cdata = re.findall(r'Status="[\s\S]*>', msg)
    cdata = get_value("StartTime", msg)
    datetime_list = []
    for i in range(len(cdata)):
        temp = cdata[i].replace("T", " ")
        # 判断日期是否比当前时间小
        datetime_list.append(temp)
    return datetime_list


def time_compare(datetime1):
    nowtime = datetimeall()
    d1 = datetime.datetime.strptime(datetime1, '%Y-%m-%d %H:%M:%S')
    d2 = datetime.datetime.strptime(nowtime, '%Y-%m-%d %H:%M:%S')
    if d1 >= d2:
        return True
    else:
        return False
