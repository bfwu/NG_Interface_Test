# -*- coding: utf-8 -*-
"""
这是国标
Created on 2018-07-11
@author: lenovo
"""
from src.test.public import date
from src.test.public import base_info
from src.test.public import add_character
from src.test.public import create_phone_no

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
    msg = """<?xml version="1.0" encoding="UTF-8"?>
    <OnlineTicketingServiceQuery Version="1.0" Datetime="2018-07-11T10:42:41" Username="{Username}" Password="e10adc3949ba59abbe56e057f20f883e">
        <QueryFilm EndDate="{EndDate}" Id="ID_QueryFilm" StartDate="{StartDate}"></QueryFilm>
        <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
            <ds:SignedInfo>
                <ds:CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments"/>
                <ds:SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>
                <ds:Reference URI="#ID_QueryFilm">
                    <ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
                    <ds:DigestValue>MIx+dTip2q8YZuszc1u9FjgstNEn0TX88Pvn9Uc2qho=</ds:DigestValue>
                </ds:Reference>
            </ds:SignedInfo>
            <ds:SignatureValue></ds:SignatureValue>
        </ds:Signature>
    </OnlineTicketingServiceQuery>"""
    # 匹配日期
    msg = msg.format(EndDate=today, StartDate=today, Username=net_user)
    return msg


# 查询影院信息
def cinema_info_xml():
    msg = """<?xml version="1.0" encoding="utf-8"?>
    
    <OnlineTicketingServiceQuery Version="1.0" Datetime="2018-07-18T11:22:38" Username="{Username}" Password="e10adc3949ba59abbe56e057f20f883e">
      <QueryCinema CinemaCode="{CinemaCode}" Id="ID_QueryCinema"/>
      <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
        <ds:SignedInfo>
          <ds:CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments"/>
          <ds:SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>
          <ds:Reference URI="#ID_QueryCinema">
            <ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
            <ds:DigestValue>uR5E53cCgApIHGD7EVShRDCG2NY=</ds:DigestValue>
          </ds:Reference>
        </ds:SignedInfo>
        <ds:SignatureValue/>
      </ds:Signature>
    </OnlineTicketingServiceQuery>"""
    # 替换影院编码
    msg = msg.format(CinemaCode=cinema_code, Username=net_user)
    return msg


# 查询有放映计划的影厅座位信息
def plan_hall_seat_xml():
    msg = """   
        <OnlineTicketingServiceQuery Version="1.0" Datetime="2018-7-12T15:19:42" Username="{Username}" Password="e10adc3949ba59abbe56e057f20f883e">
          <QuerySeat CinemaCode="{CinemaCode}" Id="ID_QuerySeat" ScreenCode="{ScreenCode}"/>  
          <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">  
            <ds:SignedInfo>
              <ds:CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments"/>  
              <ds:SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>
              <ds:Reference URI="#ID_QuerySeat">
                <ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
                <ds:DigestValue>/jiYOvaH5Zm8BpuyyKnw7gl7bYY=</ds:DigestValue>
              </ds:Reference>
            </ds:SignedInfo>
            <ds:SignatureValue/>
          </ds:Signature>
        </OnlineTicketingServiceQuery>"""
    # 查找影院编码并替换
    msg = msg.format(CinemaCode=cinema_code, ScreenCode=screen_code, Username=net_user)
    return msg


# 查询放映计划
def film_plan_xml():
    msg = """
    <?xml version="1.0" encoding="utf-8"?>  
    <OnlineTicketingServiceQuery Version="1.0" Datetime="2018-7-11T15:33:02" Username="{Username}" Password="e10adc3949ba59abbe56e057f20f883e">
      <QuerySession CinemaCode="{CinemaCode}" EndDate="{EndDate}" Id="ID_QuerySession" StartDate="{EndDate}"/>
      <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
        <ds:SignedInfo>
          <ds:CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments"/>
          <ds:SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>
          <ds:Reference URI="#ID_QuerySession">
            <ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
            <ds:DigestValue>aG8cKmcerYkgQWABHQaJ8m8LxgI=</ds:DigestValue>
          </ds:Reference>
        </ds:SignedInfo>
        <ds:SignatureValue/>
      </ds:Signature>
    </OnlineTicketingServiceQuery>
    """
    # 替换网络用户
    msg = msg.format(CinemaCode=cinema_code, EndDate=today, StartDate=today, Username=net_user)
    return msg


# 查询放映计划可用座位
def plan_seat_xml(film_plan):
    """
    :param film_plan:放映计划
    :return:
    """
    msg = """
    <?xml version="1.0" encoding="utf-8"?>
    <OnlineTicketingServiceQuery Version="1.0" Datetime="2018-7-16T15:36:13" Username="{Username}" Password="e10adc3949ba59abbe56e057f20f883e">
      <QuerySessionSeat CinemaCode="{CinemaCode}" Id="ID_QuerySessionSeat" SessionCode="{SessionCode}" Status="All"/>
      <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
        <ds:SignedInfo>
          <ds:CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments"/>
          <ds:SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>
          <ds:Reference URI="#ID_QuerySessionSeat">
            <ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
            <ds:DigestValue>dPECdCVUJJMzrU/LLGoIfp/ODIA=</ds:DigestValue>
          </ds:Reference>
        </ds:SignedInfo>
        <ds:SignatureValue/>
      </ds:Signature>
    </OnlineTicketingServiceQuery>    
        """
    msg = msg.format(CinemaCode=cinema_code, Username=net_user, SessionCode=film_plan)
    return msg


# 锁座
def lock_seat_xml(session_code, seat_code):
    """
    :param session_code:放映计划
    :param seat_code: 座位号
    :return:
    """
    msg = """<?xml version="1.0" encoding="utf-8"?>
    <OnlineTicketingServiceQuery Version="1.0" Datetime="2018-7-16T16:02:55" Username="{Username}" Password="e10adc3949ba59abbe56e057f20f883e">
      <LockSeat CinemaCode="{CinemaCode}" Id="ID_LockSeat">
        <Order Count="1" SessionCode="{SessionCode}">
          <Seat SeatCode="{SeatCode}"/>
        </Order>
      </LockSeat>
      <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
        <ds:SignedInfo>
          <ds:CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments"/>
          <ds:SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>
          <ds:Reference URI="#ID_LockSeat">
            <ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
            <ds:DigestValue>0xj1XmuDfw5AyH4cxq6ZMsdOsMA=</ds:DigestValue>
          </ds:Reference>
        </ds:SignedInfo>
        <ds:SignatureValue/>
      </ds:Signature>
    </OnlineTicketingServiceQuery>"""
    msg = msg.format(CinemaCode=cinema_code, Username=net_user, SessionCode=session_code, SeatCode=seat_code)
    return msg


# 确认订单
def order_sure_xml(order_code, session_code, seat_code, price):
    """
    :param order_code: 订单号
    :param session_code: 放映计划
    :param seat_code: 座位编码
    :param price: 交易价格
    :return:
    """
    msg = """<?xml version="1.0" encoding="utf-8"?>

    <OnlineTicketingServiceQuery Version="1.0" Datetime="2018-07-18T16:38:08" Username="{Username}" Password="e10adc3949ba59abbe56e057f20f883e">
      <SubmitOrder CinemaCode="{CinemaCode}" Id="ID_SubmitOrder">
        <Order Count="1" OrderCode="{OrderCode}" SessionCode="{SessionCode}">
          <Seat Price="{Price}" SeatCode="{SeatCode}"/>
        </Order>
      </SubmitOrder>
      <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
        <ds:SignedInfo>
          <ds:CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments"/>
          <ds:SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>
          <ds:Reference URI="#ID_SubmitOrder">
            <ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
            <ds:DigestValue>N0+Lzz/Q01X+0sDYc8CxEaalbuo=</ds:DigestValue>
          </ds:Reference>
        </ds:SignedInfo>
        <ds:SignatureValue/>
      </ds:Signature>
    </OnlineTicketingServiceQuery>"""
    # 替换影院编码
    msg = msg.format(Username=net_user, CinemaCode=cinema_code, OrderCode=order_code, SessionCode=session_code,
                     price=price, SeatCode=seat_code)
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


# 查询出票状态
def query_print(print_no, verify_code):
    """
    :param print_no: 取票号
    :param verify_code: 验证码
    :return:
    """
    msg = """
    <?xml version="1.0" encoding="UTF-8"?>

    <OnlineTicketingServiceQuery Version="1.0" Datetime="2018-08-03T14:31:22" Username="{Username}" Password="e10adc3949ba59abbe56e057f20f883e">
    <QueryPrint CinemaCode="{CinemaCode}" Id="ID_QueryPrint">
    <Order>
    <PrintNo>{PrintNo}</PrintNo>
    <VerifyCode>{VerifyCode}</VerifyCode>
    </Order>
    </QueryPrint>
    </OnlineTicketingServiceQuery>
    """
    # 替换影院编码
    msg = msg.format(CinemaCode=cinema_code, Username=net_user, PrintNo=print_no, VerifyCode=verify_code)
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


# 查询订单
def query_order(oder_code):
    """

    :param oder_code: 订单号
    :return:
    """
    msg = """
          <?xml version="1.0" encoding="UTF-8"?> 
      
      <OnlineTicketingServiceQuery Version="1.0" Datetime="2018-08-03T14:31:22" Username="{Username}" Password="e10adc3949ba59abbe56e057f20f883e">
     <QueryOrder CinemaCode="{CinemaCode}" Id="ID_QueryOrder">
     <OrderCode>{OrderCode}</OrderCode>
     </QueryOrder>
      </OnlineTicketingServiceQuery>
    """
    # 替换影院编码
    msg = msg.format(CinemaCode=cinema_code, Username=net_user, OrderCode=oder_code)
    return msg
