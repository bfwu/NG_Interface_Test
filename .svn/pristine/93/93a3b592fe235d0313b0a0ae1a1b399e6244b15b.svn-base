# -*- coding: utf-8 -*-

import time
import unittest

import suds

from src.test.data_xml import OnlineTicketingServiceQuery_D
from src.test.data_xml import *
from src.test.data_xml.methonSelf import get_current_function_name, getAvilableSaleSeat
from src.test.public import repxml
from src.test.public.Log import logger
from src.test.public.url import url_query


class SearchOrderInfo(unittest.TestCase):
	'''查询订单信息'''
	url = url_query()
	OrderCode = '0'
	SeatCode = '0'
	PrintNo = '0'
	VerifyCode = '0'
	ServiceFee = '0'
	plan_list = []
	SeatCode = '0'
	SessionPlanCode = '0'
	
	def test_001_search_show_plan(self):
		'''查询放映计划_ID_DQuerySession'''
		global SessionPlanCode
		requestName = get_current_function_name()
		client = suds.client.Client(self.url)
		xml = OnlineTicketingServiceQuery_D.film_plan_xml()
		res = client.service['NetSaleWebServicePort'].query(xml)

		self.assertEqual(repxml.get_status(res), 'Success')
		SessionPlanCode = repxml.get_value("Code", res)[0]
		logger.info(requestName + '--' + repxml.get_keyOfValue("ErrorMessage", res) + "SessionPlanCode" + ':' + SessionPlanCode)
	
	def test_002_plan_seat_xml(self):
		'''查询放映计划可用座位_ID_DQuerySessionSeat'''
		requestName = get_current_function_name()
		global SeatCode
		client = suds.client.Client(self.url)
		xml = OnlineTicketingServiceQuery_D.plan_seat_xml(SessionPlanCode)
		res = client.service['NetSaleWebServicePort'].query(xml)
		
		self.assertEqual(repxml.get_status(res), 'Success')
		SeatCode = getAvilableSaleSeat(res)
		logger.info(requestName + '--' + repxml.get_keyOfValue("ErrorMessage", res) + "SeatCode" + ':' + SeatCode)
	
	def test_003_lock_seat_xml(self):
		'''锁定座位_ID_DLockSeat'''
		requestName = get_current_function_name()
		global OrderCode
		client = suds.client.Client(self.url)
		xml = OnlineTicketingServiceQuery_D.lock_seat_xml(SessionPlanCode, SeatCode)
		res = client.service['NetSaleWebServicePort'].query(xml)
		
		OrderCode = repxml.get_keyOfValue("OrderCode", res)
		logger.info(requestName + '--' + repxml.get_keyOfValue("ErrorMessage", res) + "OrderCode" + ':' + OrderCode)
		self.assertEqual(repxml.get_status(res), 'Success')
	
	def test_004_confirmSCTS_order(self):
		'''确认SCTS订单交易接口_ID_SubmitOrder'''
		global PrintNo, VerifyCode
		requestName = get_current_function_name()
		client = suds.client.Client(self.url)
		xml = OnlineTicketingServiceQuery_D.order_sure_xml(OrderCode, SessionPlanCode, SeatCode, '50', '40', '10', '3')
		res = client.service['NetSaleWebServicePort'].query(xml)
		
		PrintNo = repxml.get_keyOfValue("PrintNo", res)
		VerifyCode = repxml.get_keyOfValue("VerifyCode", res)
		logger.info(requestName + '--' + repxml.get_keyOfValue("ErrorMessage", res))
		self.assertEqual(repxml.get_status(res), 'Success')
	
	def test_005_refund_ticket(self):
		'''退票接口_ID_RefundTicket'''
		requestName = get_current_function_name()
		client = suds.client.Client(self.url)
		xml = OnlineTicketingServiceQuery_D.refound_ticket(PrintNo, VerifyCode)
		res = client.service['NetSaleWebServicePort'].query(xml)
		
		logger.info(requestName + '--' + repxml.get_keyOfValue("ErrorMessage",res) + "PrintNo" + ':' + PrintNo + "VerifyCode" + ':' + VerifyCode)
		self.assertEqual(repxml.get_status(res), 'Success')
		
	def test_006_second_refund_ticket(self):
		'''已经退票再次退票_ID_RefundTicket'''
		requestName = get_current_function_name()
		client = suds.client.Client(self.url)
		xml = OnlineTicketingServiceQuery_D.refound_ticket(PrintNo, VerifyCode)
		res = client.service['NetSaleWebServicePort'].query(xml)
		
		logger.info(requestName + '--' + repxml.get_keyOfValue("ErrorMessage",res) + "PrintNo" + ':' + PrintNo + "VerifyCode" + ':' + VerifyCode)
		self.assertEqual(repxml.get_status(res), 'Failure')
		self.assertEqual(repxml.get_keyOfValue("ErrorMessage",res),'退票失败,取票号或验证码查不到影票信息')