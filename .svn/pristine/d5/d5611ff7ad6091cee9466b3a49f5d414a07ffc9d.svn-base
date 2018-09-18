# -*- coding: utf-8 -*-
# 获取所有座位
from src.test.public import repxml
import inspect

def getAvilableSaleSeat(res):
	seat_all = repxml.get_value("Code", res)
	# 获取座位可售状态
	status = repxml.get_value("Status", res)
	# 获取可买座位
	seat = []
	for j in range(len(status)):
		if status[j] == "Available":
			seat.append(seat_all[j])
	return seat[0]

def get_current_function_name():
    return inspect.stack()[1][3]