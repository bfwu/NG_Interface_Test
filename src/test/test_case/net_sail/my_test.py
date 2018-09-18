# -*- coding: utf-8 -*-

"""
Created on 2018-07-11
@author: lenovo
"""

import suds

from src.test.data_xml import OnlineTicketingServiceQuery
from src.test.public import repxml
from src.test.public.url import url_query


# 获取影片信息
def get_film_info():
    url = url_query()
    client = suds.client.Client(url)
    xml = OnlineTicketingServiceQuery.film_info_xml()
    res = client.service['NetSaleWebServicePort'].query(xml)


# 获取影院的影厅信息
def get_cinema_info():
    url = url_query()
    client = suds.client.Client(url)
    xml = OnlineTicketingServiceQuery.cinema_info_xml()
    res = client.service['NetSaleWebServicePort'].query(xml)
    # 后别这块加一下如果没有影厅的处理
    cinema_info = []
    cinema_code = repxml.get_value("Code", res)
    cinema_name = repxml.get_value("Name", res)
    cinema_info.append(cinema_code)
    cinema_info.append(cinema_name)
    return cinema_info


# 获取放映计划。获取到当前日放映计划列表,剔除已經開售的放映计划
def get_film_plan():
    # 所有放映计划列表信息
    plan_list = []
    url = url_query()
    client = suds.client.Client(url)
    xml = OnlineTicketingServiceQuery.film_plan_xml()
    res = client.service['NetSaleWebServicePort'].query(xml)
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
def get_plan_nomal_seat():
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


# 根据放映计划获取可购买座位，返回排期和该排期的所有座位
def get_available_seat():
    film_plan_seat = []
    if len(film_plan_seat) == 0:
        return film_plan_seat
    else:
        url = url_query()
        client = suds.client.Client(url)
        plan_list = get_film_plan()
        # # 获取一下可购买影票的影厅
        # for i in range(len(plan_list[0])):
        #     if plan_list[1][i] not in hall_code:
        #         hall_code.append(plan_list[1][i])
        # 排期+排期的座位 film_plan_seat[0]是所有排期，后边全部是可选座位
        film_plan_seat.append(plan_list[0])
        for i in range(len(plan_list[0])):
            xml = OnlineTicketingServiceQuery.plan_seat_xml(plan_list[0][i])
            # 选取一个影厅获取可购买座位
            res = client.service['NetSaleWebServicePort'].query(xml)
            # 获取所有座位
            seat_all = repxml.get_value("Code", res)
            # 获取座位可售状态
            status = repxml.get_value("Status", res)
            # 获取可买座位
            seat = []
            for j in range(len(status)):
                if status[j] == "Available":
                    seat.append(seat_all[j])
            film_plan_seat.append(seat)
        # 返回的是放映计划加上座位列表
        return film_plan_seat


# 锁座
def lock_seat():
    lock_info = []
    url = url_query()
    client = suds.client.Client(url)
    # 顺序为 放映计划，放映时间，放映大厅code，大厅名称，电影名称，最低票价，标准票价
    film_plan = get_film_plan()
    # 放映计划为空，直接返回空
    if len(film_plan) < 1:
        print("今日没有放映计划，请添加计划")
        return lock_info
    else:
        # 放映计划+座位
        film_plan_seat = get_available_seat()
        # 大厅编码+座位
        hall_seat = get_plan_nomal_seat()
        cinema_info = get_cinema_info()
        # 做一下可买座位和可用座位的匹配，去除情侣座位
        temp = []
        # 需要先标记在删除

        # 如果放映计划为空，则直接提示停止
        if len(film_plan_seat[0]) < 1:
            print("今日没有放映计划或电影已开场，请添加计划后再尝试")
            return lock_info
        else:
            # 如果该计划下已经没有座位则重新选取放映计划
            for p in range(len(film_plan_seat[0])):
                if len(film_plan_seat[p + 1]) > 0:
                    xml = OnlineTicketingServiceQuery.lock_seat_xml(film_plan_seat[0][p], film_plan_seat[p + 1][0])
                    res = client.service['NetSaleWebServicePort'].query(xml)
                    # 获取订单信息,这块情侣座不能单卖，那么就要跳过情侣座 明天搞
                    order_code = repxml.get_order_code(res)
                    ordercode = order_code[0]
                    for i in range(len(film_plan[0])):
                        if film_plan_seat[0][0] in film_plan[0][i]:
                            filmplan = film_plan[0][i]
                            starttime = film_plan[1][i]
                            hallcode = film_plan[2][i]
                            filmname = film_plan[3][i]
                            lowest = film_plan[4][i]
                            stander = film_plan[5][i]
                            break
                    for j in range(len(cinema_info[0])):
                        if hallcode in cinema_info[0][j]:
                            hallname = cinema_info[1][j]
                            break
                else:
                    continue
                print("订单编号是：%s" % ordercode)
                print("订单的放映计划是：%s" % filmplan)
                print("订单的放映时间是：%s" % starttime)
                print("订单的影厅编码是：%s" % hallcode)
                print("订单的影厅名称是：%s" % hallname)
                print("订单的影片是：%s" % filmname)
                print("订单的座位是：%s" % film_plan_seat[1][1])
                print("订单的最低票价是：%s" % lowest)
                print("订单的标准票价是：%s" % stander)

                # 订单
                lock_info.append(ordercode)
                # 放映计划
                lock_info.append(filmplan)
                # 座位
                lock_info.append(film_plan_seat[1][0])
                # 价格
                lock_info.append(stander)
                break
        return lock_info
        # 确认订单


def order_sure():
    lockseat = lock_seat()
    if len(lockseat) != 0:
        url = url_query()
        client = suds.client.Client(url)
        xml = OnlineTicketingServiceQuery.order_sure_xml(lockseat[0], lockseat[1], lockseat[2], lockseat[3])
        res = client.service['NetSaleWebServicePort'].query(xml)
        status = repxml.get_status(res)
        if status == "Success":
            print("购买1张票成功")
        else:
            print(repxml.get_error_message(res))


if __name__ == "__main__":
 order_sure()
    # get_film_info()
    # for i in range(100):
    #     order_sure()
