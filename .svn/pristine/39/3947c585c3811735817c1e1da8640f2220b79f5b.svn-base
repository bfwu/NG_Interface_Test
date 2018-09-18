# -*- coding: utf-8 -*-
import string
import unittest
import time

import suds
from src.test.data_xml import OnlineTicketingServiceQuery_D
from src.test.data_xml.methonSelf import getAvilableSaleSeat, get_current_function_name
from src.test.public import repxml
from src.test.public.Log import logger
from src.test.public.url import url_query
from src.test.public import date

class NoMemberBuyTicker(unittest.TestCase):
	url = url_query()
	OrderCode = '0'
	SeatCode = '0'
	PrintNo = '0'
	VerifyCode = '0'
	ServiceFee = '0'
	plan_list=[]
	SeatCode='0'
	SessionPlanCode='0'
	# currentTime=datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
	
	


	def test_001_searchShowPlanInfo(self):
		'''查询放映计划'''
		global SessionPlanCode
		requestName = get_current_function_name()
		client = suds.client.Client(self.url)
		xml = OnlineTicketingServiceQuery_D.film_plan_xml()
		res = client.service['NetSaleWebServicePort'].query(xml)
		status = repxml.get_status(res)
		self.assertEqual(status, 'Success')
		SessionPlanCode= repxml.get_value("Code", res)[0]
		logger.info(requestName + '--' + repxml.get_keyOfValue("ErrorMessage", res) + "SessionPlanCode" + ':'+SessionPlanCode)
		
	
	
	def test_002_plan_seat_xml(self):
		'''查询放映计划可用座位'''
		global SeatCode
		requestName = get_current_function_name()
		client = suds.client.Client(self.url)
		xml = OnlineTicketingServiceQuery_D.plan_seat_xml(SessionPlanCode)
		res = client.service['NetSaleWebServicePort'].query(xml)
		status = repxml.get_status(res)
		self.assertEqual(status, 'Success')
		SeatCode=getAvilableSaleSeat(res)
		logger.info(requestName + '--' + repxml.get_keyOfValue("ErrorMessage", res) + "SeatCode" + ':' + SeatCode)
	

	def test_003_lock_seat_xml(self):
		'''锁定座位（D）'''
		global OrderCode
		requestName = get_current_function_name()
		client = suds.client.Client(self.url)
		xml = OnlineTicketingServiceQuery_D.lock_seat_xml(SessionPlanCode,SeatCode)
		res = client.service['NetSaleWebServicePort'].query(xml)
		status = repxml.get_status(res)
		OrderCode = repxml.get_keyOfValue("OrderCode", res)
		self.assertEqual(status, 'Success')
		logger.info(requestName + '--' + repxml.get_keyOfValue("ErrorMessage", res) + "OrderCode" + ':' + OrderCode)
		
	def test_004_confirmSCTSOrder(self):
		'''确认SCTS订单交易接口'''
		global PrintNo, VerifyCode
		requestName = get_current_function_name()
		client = suds.client.Client(self.url)
		xml = OnlineTicketingServiceQuery_D.order_sure_xml(OrderCode, SessionPlanCode, SeatCode, '50', '40', '10', '3')
		res = client.service['NetSaleWebServicePort'].query(xml)
		status = repxml.get_status(res)
		PrintNo = repxml.get_keyOfValue("PrintNo", res)
		VerifyCode = repxml.get_keyOfValue("VerifyCode", res)
		logger.info(requestName + '--' + repxml.get_keyOfValue("ErrorMessage", res)+"PrintNo" + ':' + PrintNo+"VerifyCode" + ':' + VerifyCode)
		self.assertEqual(status, 'Success')
		
	def test_005_takeTicketConfirm(self):
		'''取票确认信息接口'''
		requestName = get_current_function_name()
		client = suds.client.Client(self.url)
		xml = OnlineTicketingServiceQuery_D.take_ticket_info(PrintNo, VerifyCode)
		res = client.service['NetSaleWebServicePort'].query(xml)
		logger.info(requestName + '--' + repxml.get_keyOfValue("ErrorMessage", res))
		status = repxml.get_status(res)
		self.assertEqual(status, 'Success')
		
	def test_006_recordTicketInfo(self):
		'''记录信息'''
		currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		with open('buyTicketInfo.txt', 'a') as text:
			text.write('%s=%s' % ('testcaseTime', currentTime))
			text.write('%s=%s' % ('SessionPlanCode', SessionPlanCode))
			text.write('%s=%s' % ('SeatCode', SeatCode))
			text.write('%s=%s' % ('OrderCode', OrderCode))
			text.write('%s=%s' % ('PrintNo', PrintNo))
			text.write('%s=%s' % ('VerifyCode', VerifyCode))
			text.write("\n")
	