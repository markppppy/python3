#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : used_mulprocessing.py
# @Desc    : 
# @Time    : 2021/5/29 15:23
# @Author  : songpeiyao
# @Version : 1.0
import multiprocessing


def fetch_data_and_predict(num):
    print(num)


# 把数据分成5分，每次循环通过同一个方法中的参数，取不同的数据
p = None
for i in range(5):
    p = multiprocessing.Process(target=fetch_data_and_predict, args=(i,))
    p.start()
p.join()  # 等所有job运行完，才继续后面的步骤

