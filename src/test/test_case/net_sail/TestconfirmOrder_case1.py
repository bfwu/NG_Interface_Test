# -*- coding: utf-8 -*-
import unittest

import suds

from src.test.data_xml import OnlineTicketingServiceQuery
from src.test.public import repxml
from src.test.public.url import url_query


# 获取影片信息
class TestConfirmOrder(unittest.TestCase):
    def  test_001_get_film_info(self):
        '''获取影院信息'''
        url = url_query()
        client = suds.client.Client(url)
        xml = OnlineTicketingServiceQuery.film_info_xml()
        rp=client.service['NetSaleWebServicePort'].query(xml)
        print rp
        
        status = repxml.get_status(rp)
        self.assertEqual(status, 'Success')

        

    # 获取影院的影厅信息
    def test_002_get_cinema_info(self):
        url = url_query()
        client = suds.client.Client(url)
        xml = OnlineTicketingServiceQuery.cinema_info_xml()
        res = client.service['NetSaleWebServicePort'].query(xml)
        status = repxml.get_status(res)
        self.assertEqual(status, 'Success')
        # 后别这块加一下如果没有影厅的处理
        cinema_info = []
        cinema_code = repxml.get_value("Code", res)
        cinema_name = repxml.get_value("Name", res)
        cinema_info.append(cinema_code)
        cinema_info.append(cinema_name)
        return cinema_info
# 获取放映计划。获取到当前日放映计划列表,剔除已經開售的放映计划
    def test_003_get_film_plan(self):
        # 所有放映计划列表信息
        plan_list = []
        url = url_query()
        client = suds.client.Client(url)
        xml = OnlineTicketingServiceQuery.film_plan_xml()
        res = client.service['NetSaleWebServicePort'].query(xml)

        status = repxml.get_status(res)
        self.assertEqual(status, 'Success')
        # 先判断一下是否有放映计划
        error_code = repxml.get_error_code(res)
        if len(error_code) > 0:
            print(repxml.get_error_message(res))
            return plan_list
        else:
            # 获取放映计划列表
            # 放映计划iD
            film_planx = repxml.get_value("Code", res)
            # 因为返回的xml中有两个code，一个是放映计划，一个是影片的code，需要删除影片code
            film_plan = []
            start_time = []
            for i in range(len(film_planx)):
                if len(film_planx[i]) > 12:
                    film_plan.append(film_planx[i])
            # 放映计划的影厅
            film_hall = repxml.get_screen_code(res)
            # 影片名称
            film_name = repxml.get_value("Name", res)
            # 放映时间
            start_timex = repxml.get_value("StartTime", res)
            # 调整时间格式
            for t in range(len(start_timex)):
                temp = start_timex[t].replace("T", " ")
                start_time.append(temp)
            # 最低票价
            lowest_price = repxml.get_value("LowestPrice", res)
            # 标准票价
            standard_price = repxml.get_value("StandardPrice", res)
            plan_list.append(film_plan)
            plan_list.append(start_time)
            plan_list.append(film_hall)
            plan_list.append(film_name)
            plan_list.append(lowest_price)
            plan_list.append(standard_price)
            # 处理小于当前日期的放映计划
            temp = []
            for i in range(len(plan_list[0])):
                if repxml.time_compare(plan_list[1][i]) == 0:
                    temp.append(i)
            temp.sort()
            temp.reverse()
            for p in range(len(plan_list)):
                for q in range(len(temp)):
                    del plan_list[p][temp[q]]
            if len(plan_list[0]) == 0:
                plan_list = []
                return plan_list
            else:
                return plan_list
# 获取影厅的座位信息，这里排除情侣座，情侣座不能单独卖票,返回所有影厅的可用座位信息，除去情侣座
    def test_004_get_plan_nomal_seat():
        # 可用的座位除去情侣座
        seat_status_type = []
        # 返回的数组，包含影厅和座位
        hall_seat = []
        # 第三个参数是影厅
        film_plan = get_film_plan()
        # 没有放映计划就不查座位了
        if len(film_plan) < 1:
            return seat_status_type
        else:
            url = url_query()
            client = suds.client.Client(url)
            # 影厅去重
            hall_code = list(set(film_plan[2]))
            hall_seat.append(hall_code)
            # 获取所有影厅的座位
            for i in range(len(hall_code)):
                xml = OnlineTicketingServiceQuery.plan_hall_seat_xml(hall_code[i])
                res = client.service['NetSaleWebServicePort'].query(xml)
                seat_code = repxml.get_value("Code", res)
                seat_status = repxml.get_value("Status", res)
                seat_lovers = repxml.get_value("Lovers", res)
                seat_status_type.append(seat_code)
                seat_status_type.append(seat_status)
                seat_status_type.append(seat_lovers)
                # 先删除不可用座位
                temp = []
                for a in range(len(seat_status_type[0])):
                    if seat_status_type[1][a] != 'Available':
                        temp.append(a)
                if len(temp) > 0:
                    temp.reverse()
                    for a in range(len(temp)):
                        del seat_status_type[0][temp[a]]
                        del seat_status_type[1][temp[a]]
                        del seat_status_type[2][temp[a]]
                # 删除情侣座位
                temp1 = []
                for j in range(len(seat_status_type[0])):
                    if seat_status_type[2][j] != "":
                        temp1.append(j)
                if len(temp1) > 0:
                    temp1.reverse()
                    for a in range(len(temp)):
                        del seat_status_type[0][temp[a]]
                        del seat_status_type[1][temp[a]]
                        del seat_status_type[2][temp[a]]
                seat_status.append(seat_status_type[0])
            return seat_status_type
