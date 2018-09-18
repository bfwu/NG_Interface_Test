# -*- coding: utf-8 -*-
"""
这是私标
Created on 2018-09-03
@author: lenovo
"""

from src.test.public import date
from src.test.public import base_info
from src.test.public import add_character
from src.test.public import create_phone_no
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
cinema_code = base_info.cinema_code()
screen_code = base_info.screen_code()
net_user = base_info.net_user_name()
channel_id = base_info.net_channel_id()
channel_name = base_info.net_channel_name()
channel_order_no = add_character.add_code_by_need(3) + create_phone_no.createphoneno()
today = date.date()


# 查询影片信息
def film_info_xml():
    u"""查询影片信息"""
    msg = """ <?xml version="1.0" encoding="UTF-8"?>     
      <OnlineTicketingServiceQuery Version="1.0" Datetime="2018-08-03T14:31:22" Username="{Username}" Password="e10adc3949ba59abbe56e057f20f883e">
      <DQueryFilm EndDate="{EndDate}" Id="ID_DQueryFilm" StartDate="{StartDate}"></DQueryFilm>
      </OnlineTicketingServiceQuery>
      """
    msg = msg.format(Username=net_user, EndDate=today, StartDate=today)
    return msg


# 查询影厅座位信息
def hall_seat_xml(screen_code):
    """

    :param screen_code: 影厅编码
    :return:
    """
    msg = """   
        <?xml version="1.0" encoding="UTF-8"?>     
      <OnlineTicketingServiceQuery Version="1.0" Datetime="2018-08-03T14:31:22" Username="{Username}" Password="e10adc3949ba59abbe56e057f20f883e">
      <DQuerySeat CinemaCode="{CinemaCode}" Id="ID_DQuerySeat" ScreenCode="{ScreenCode}">
      </DQuerySeat>
      </OnlineTicketingServiceQuery>
        """
    # 替换网络用户
    msg = msg.format(Username=net_user, CinemaCode=cinema_code, ScreenCode=screen_code)
    return msg


# 查询放映计划
def film_plan_xml():
    msg = """
    <?xml version="1.0" encoding="UTF-8"?> 
      
      <OnlineTicketingServiceQuery Version="1.0" Datetime="2018-08-03T14:31:22" Username="{Username}" Password="e10adc3949ba59abbe56e057f20f883e">
     <DQuerySession ChannelId="{ChannelId}" CinemaCode="{CinemaCode}" EndDate="{EndDate}" Id="ID_DQuerySession" StartDate="{StartDate}">
     </DQuerySession>
      </OnlineTicketingServiceQuery>
    """
    # 替换网络用户
    msg = msg.format(Username=net_user, CinemaCode=cinema_code, ChannelId=channel_id, StartDate=today, EndDate=today)
    return msg


# 查询放映计划可用座位
def plan_seat_xml(film_plan):
    """

    :param film_plan: 放映计划
    :return:
    """
    msg = """
       <?xml version="1.0" encoding="UTF-8"?>   
      <OnlineTicketingServiceQuery Version="1.0" Datetime="2018-08-03T14:31:22" Username="{Username}" Password="e10adc3949ba59abbe56e057f20f883e">
      <DQuerySessionSeat ChannelId="{ChannelId}" CheckChannel="1" CinemaCode="{CinemaCode}" Id="ID_DQuerySessionSeat" SessionCode="{SessionCode}" Status="Available" channelName="{channelName}">
      </DQuerySessionSeat>
      </OnlineTicketingServiceQuery>    
        """
    # 替换网络用户
    msg = msg.format(Username=net_user, CinemaCode=cinema_code, ChannelId=channel_id, channelName=channel_name,
                     SessionCode=film_plan)
    return msg


# 锁座
def lock_seat_xml(session_code, seat_code):
    """
    :param session_code:放映计划
    :param seat_code: 座位编码
    :return:
    """
    msg = """
         <?xml version="1.0" encoding="UTF-8"?>   
      <OnlineTicketingServiceQuery Version="1.0" Datetime="2018-08-03T17:38:58" Username="{Username}" Password="e10adc3949ba59abbe56e057f20f883e">
      <DLockSeat CheckChannel="1" CinemaCode="{CinemaCode}" Id="ID_DLockSeat">
      <Order ChannelId="{ChannelId}" channelName="{channelName}" Count="1" SessionCode="{SessionCode}" Timestamp="2018-08-03 17:38:58">
      <Seat SeatCode="{SeatCode}"></Seat>
      <channelId>{ChannelId}</channelId>
      <channelName>{channelName}</channelName>
      <timestamp>2018-08-03 17:38:58</timestamp>
      </Order>
      </DLockSeat>
      </OnlineTicketingServiceQuery>
    """
    msg = msg.format(Username=net_user, CinemaCode=cinema_code, ChannelId=channel_id, channelName=channel_name,
                     SessionCode=session_code, SeatCode=seat_code)
    return msg


# 确认订单
def order_sure_xml(order_code, session_code, seat_code, price, pay_price, service_fee, net_service_fee):
    """
    :param order_code:订单号
    :param session_code: 放映计划
    :param seat_code: 座位号
    :param price: 销售价
    :param pay_price: 结算价
    :param service_fee: 服务费
    :param net_service_fee: 网售服务费
    :return:
    """
    msg = """
          <?xml version="1.0" encoding="UTF-8"?> 
      
      <OnlineTicketingServiceQuery Version="1.0" Datetime="2018-08-03T14:31:22" Username="{Username}" Password="e10adc3949ba59abbe56e057f20f883e">
      <SubmitSCTSOrder CheckChannel="1" CinemaCode="{CinemaCode}" Id="ID_SubmitOrder">
      <Order ChannelId="{ChannelId}" ChannelName="{ChannelName}" ChannelOrderNo="{ChannelOrderNo}" Count="1" OrderCode="{OrderCode}" OrderPhone="18591786769" SessionCode="{SessionCode}">
      <Seat NetServiceFee="{NetServiceFee}" PayPrice="{PayPrice}" Price="{Price}" SeatCode="{SeatCode}" ServiceFee="{ServiceFee}"></Seat>
      <channelOrderNo>{ChannelOrderNo}</channelOrderNo>
      </Order>
      </SubmitSCTSOrder>
      </OnlineTicketingServiceQuery>
    """
    # 替换影院编码
    msg = msg.format(CinemaCode=cinema_code, Username=net_user, ChannelId=channel_id, ChannelName=channel_name,
                     OrderCode=order_code, SessionCode=session_code, SeatCode=seat_code, Price=price,
                     PayPrice=pay_price, ServiceFee=service_fee, NetServiceFee=net_service_fee,
                     ChannelOrderNo=channel_order_no)
    return msg


# 解锁
def release_seat(order_code, session_code, seat_code):
    """
    :param order_code: 订单号
    :param session_code: 放映计划
    :param seat_code: 座位编码
    :return:
    """
    msg = """
        <?xml version="1.0" encoding="UTF-8"?>
      <OnlineTicketingServiceQuery Version="1.0" Datetime="2018-08-03T14:31:22" Username="{Username}" Password="e10adc3949ba59abbe56e057f20f883e">
      <ReleaseSeat CinemaCode="{CinemaCode}" Id="ID_ReleaseSeat">
      <Order Count="1" OrderCode="{OrderCode}" SessionCode="{SessionCode}">
      <Seat SeatCode="{SeatCode}"></Seat>
      </Order>
      </ReleaseSeat>
      </OnlineTicketingServiceQuery>
    """
    # 替换影院编码
    msg = msg.format(CinemaCode=cinema_code, Username=net_user, OrderCode=order_code, SessionCode=session_code,
                     SeatCode=seat_code)
    return msg


# 退票接口
def refound_ticket(print_no, verify_code):
    """
    :param print_no: 取票号
    :param verify_code: 验证码
    :return:
    """
    msg = """
          <?xml version="1.0" encoding="UTF-8"?> 
      
      <OnlineTicketingServiceQuery Version="1.0" Datetime="2018-08-03T14:31:22" Username="{Username}" Password="e10adc3949ba59abbe56e057f20f883e">
      <RefundTicket CinemaCode="{CinemaCode}" Id="ID_RefundTicket">
      <Order>
      <PrintNo>{PrintNo}</PrintNo>
      <VerifyCode>{VerifyCode}</VerifyCode>
      </Order>
      </RefundTicket>
      </OnlineTicketingServiceQuery>
    """
    # 替换影院编码
    msg = msg.format(CinemaCode=cinema_code, Username=net_user, PrintNo=print_no, VerifyCode=verify_code)
    return msg


# 查询取票信息接口
def query_take_ticket_info(print_no, verify_code):
    """
    :param print_no: 取票号
    :param verify_code: 验证码
    :return:
    """
    msg = """          
    <?xml version="1.0" encoding="UTF-8"?>
    <OnlineTicketingServiceQuery Version="1.0" Datetime="2018-08-03T14:31:22" Username="{Username}" Password="e10adc3949ba59abbe56e057f20f883e">
    <DQueryTakeTicketInfo CinemaCode="{CinemaCode}" Id="ID_DQueryTakeTicketInfo">
    <PrintNo>{PrintNo}</PrintNo>
    <VerifyCode>{VerifyCode}</VerifyCode>
    </DQueryTakeTicketInfo>
    </OnlineTicketingServiceQuery>
    """
    # 替换影院编码
    msg = msg.format(CinemaCode=cinema_code, Username=net_user, PrintNo=print_no, VerifyCode=verify_code)
    return msg


# 确认取票信息接口
def take_ticket_info(print_no, verify_code):
    """
    :param print_no: 取票号
    :param verify_code: 验证码
    :return:
    """
    msg = """          
    <?xml version="1.0" encoding="UTF-8"?> 
      
      <OnlineTicketingServiceQuery Version="1.0" Datetime="2018-08-03T14:31:22" Username="{Username}" Password="e10adc3949ba59abbe56e057f20f883e">
      <DTakeTicketConfirm CinemaCode="{CinemaCode}" Id="ID_DTakeTicketConfirm">
      <PrintNo>{PrintNo}</PrintNo>
      <VerifyCode>{VerifyCode}</VerifyCode>
      </DTakeTicketConfirm>
      </OnlineTicketingServiceQuery>
    """
    # 替换影院编码
    msg = msg.format(CinemaCode=cinema_code, Username=net_user, PrintNo=print_no, VerifyCode=verify_code)
    return msg

