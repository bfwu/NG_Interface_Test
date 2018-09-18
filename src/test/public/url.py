# -*- coding: utf-8 -*-
"""
Created on 2018-07-11
@author: lenovo
"""
import ConfigParser
from src.test.public import alldir


def url_query():
    config = ConfigParser.ConfigParser()
    config.read(alldir.get_src_dir() + "src\\test\\conf\\conf.conf")
    return config.get("base_url", "url")+'query?wsdl'


def url_pay():
    config = ConfigParser.ConfigParser()
    config.read(alldir.get_src_dir() + "src\\test\\conf\\conf.conf")
    return config.get("base_url", "url")+'pay?wsdl'
