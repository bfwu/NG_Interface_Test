# -*- coding: utf-8 -*-
import os
import time
import unittest

import suds
import sys

from src.test.data_xml import OnlineTicketingServiceQuery_D
from src.test.data_xml.methonSelf import get_current_function_name
from src.test.public import repxml
from src.test.public.Log import logger
from src.test.public.url import url_query


class SearchShowPlan(unittest.TestCase):
	url = url_query()
	OrderCode = '0'
	SeatCode = '0'
	PrintNo = '0'
	VerifyCode = '0'
	ServiceFee = '0'
	plan_list=[]
	SeatCode='0'
	SessionPlanCode='0'
	
	def test_001_no_show_plan(self):
		'''查询放映计划_ID_DQuerySession'''
		global SessionPlanCode
		requestName = get_current_function_name()
		client = suds.client.Client(self.url)
		xml = OnlineTicketingServiceQuery_D.film_plan_xml()
		res = client.service['NetSaleWebServicePort'].query(xml)
		status = repxml.get_status(res)
		self.assertEqual(status, 'Success')
		SessionPlanCode = repxml.get_value("Code", res)[0]
		logger.info(requestName + '--' + repxml.get_keyOfValue("ErrorMessage", res) + "SessionPlanCode" + ':' + SessionPlanCode)
