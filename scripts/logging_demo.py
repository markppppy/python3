#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @File    : logging.py
# @Desc    : 
# @Time    : 2020/12/27 19:14:23
# @Author  : songpeiyao
# @Version : 1.0

import logging 

# 记录器
logger = logging.getLogger('cn.cccb.applog')
logger.setLevel(logging.DEBUG)  
# 默认是warning级别，logger的日志级别一定要是handlers中最低级别的，handle日志才能打出来

# 处理器handler
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler(filename='applog.log')
fileHandler.setLevel(logging.INFO)

# formatter格式
formatter = logging.Formatter("%(asctime)s|%(levelname)-8s|%(filename)s:%(lineno)s|%(message)s")

# 给处理器设置格式
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

# 记录器中添加处理器
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

# 设置一个过滤器
fit = logging.Filter("cn.cccb")  # 只输出log名以cn.cccb开头的日志

# 关联过滤器
# logger.addFilter(fit)
consoleHandler.addFilter(fit)


# 打印日志
logger.warning('This is warning log')
logger.info('This is info log')

# 获取日志的方式
testInfo = 'error info'
try:
    int(testInfo)
except Exception as e:
    logger.exception(e)
