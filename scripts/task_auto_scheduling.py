#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @File    : task_auto_scheduling.py
# @Desc    : 
# @Time    : 2021/01/08 17:51:47
# @Author  : songpeiyao
# @Version : 1.0

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

record_tch = {}

def clean_record():
    record_tch.clear()

if __name__ == '__main__':
    scheduler = BackgroundScheduler(timezone="Asia/Shanghai")
    # 间隔设置 每天24时10分10秒执行
    intervalTrigger = CronTrigger(hour=0, minute=10, second=10, timezone="Asia/Shanghai")
    scheduler.add_job(clean_record, intervalTrigger, id='clean_record_info')
    scheduler.start()
