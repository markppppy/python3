#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @File    : logging_rfc5424.py
# @Desc    :
# @Time    : 2020/12/28 19:33:08
# @Author  : songpeiyao
# @Version : 1.0

import os
import logging
import socket
from rfc5424logging import Rfc5424SysLogHandler, NILVALUE
import datetime

envType = os.getenv("envType")


def setting_log(info, msg):
    # 记录器
    logger = logging.getLogger('bicourseevalu')
    logger.setLevel(logging.INFO)
    # 处理器Rfc5424SysLogHandler
    hostname = socket.gethostname()
    addr = socket.gethostbyname(hostname)
    sh = Rfc5424SysLogHandler(
        address=('rsyslog.idc.cedu.cn', 517),
        facility=23,
        hostname=addr,
        appname="ps-bi-courseevalu",
        procid=NILVALUE,
        enterprise_id='18060',
        structured_data={'mdc': {'APP_BUILD_VERSION': '20201208113430-36',
                                 'APP_CONTEXT': 'bicourseevalu',
                                 'APP_VERSION': '1.0.0',
                                 'HOSTNAME': addr,
                                 'IS_CONTAINER': '1',
                                 'POOL_CODE': 'ps-bi-courseevalu',
                                 'ENV_TYPE': envType,
                                 'priority': 'INFO',
                                 'timestamp': '%s' % datetime.datetime.now().isoformat('T'),
                                 'exception': '%s' % info,
                                 'message': '%s' % msg}}
    )
    sh.setLevel(logging.INFO)
    if not logger.handlers:  # 避免日志重复输出
        logger.addHandler(sh)
    # adapter = Rfc5424SysLogAdapter(logger)
    # adapter.info('')
    logger.info('')
    logger.removeHandler(sh)


setting_log('INFO', 'THIS IS INFO')
