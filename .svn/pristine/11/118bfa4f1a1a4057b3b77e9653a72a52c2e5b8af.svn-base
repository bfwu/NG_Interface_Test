#coding=utf-8

import logging
import time
import os
import logging.handlers



#log_path = readconfigfile('projectConfig', 'log_path')
# log_path ="../result/log"
# log_path='../SoapAPI/result/log'
log_path=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'result','log')
class Log:
    def __init__(self):
        self.errorlog = os.path.join(log_path, '{0}error.log'.format(time.strftime('%Y-%m-%d')))
        self.caselog = os.path.join(log_path, '{0}case.log'.format(time.strftime('%Y-%m-%d')))
    def __printconsole(self,level,logtype, message):
        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(logtype,'a',encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        # 记录一条日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self,message):
        self.__printconsole('debug', self.errorlog,message)

    def info(self,message):
        self.__printconsole('info', self.errorlog,message)

    def warning(self,message):
        self.__printconsole('warning', self.errorlog,message)

    def error(self,message):
        self.__printconsole('error', self.errorlog,message)

    def trackcase(self,message):
        self.__printconsole('info', self.caselog, message)

logger = Log()