# -*- coding: utf-8 -*-
"""
Created on 2018-07-17
@author: lenovo
"""
import ConfigParser
from src.test.public import alldir


# 影院编码
def cinema_code():
    config = ConfigParser.ConfigParser()
    config.read(alldir.get_src_dir() + "src\\test\\conf\\conf.conf")
    return config.get("cinema_code", "code")


# 影厅编码
def screen_code():
    config = ConfigParser.ConfigParser()
    config.read(alldir.get_src_dir() + "src\\test\\conf\\conf.conf")
    return config.get("screen_code", "code")


# 网络用户名
def net_user_name():
    config = ConfigParser.ConfigParser()
    config.read(alldir.get_src_dir() + "src\\test\\conf\\conf.conf")
    return config.get("net_user", "user")


# 网络用户密码
def net_user_pass():
    config = ConfigParser.ConfigParser()
    config.read(alldir.get_src_dir() + "src\\test\\conf\\conf.conf")
    return config.get("net_user", "pass")


# 网络渠道用户id
def net_channel_id():
    config = ConfigParser.ConfigParser()
    config.read(alldir.get_src_dir() + "src\\test\\conf\\conf.conf")
    return config.get("net_channel", "id")


# 网络渠道用户name
def net_channel_name():
    config = ConfigParser.ConfigParser()
    config.read(alldir.get_src_dir() + "src\\test\\conf\\conf.conf")
    return config.get("net_channel", "name")

