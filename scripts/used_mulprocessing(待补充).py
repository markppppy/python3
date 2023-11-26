#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : used_mulprocessing.py
# @Desc    : ipynb文件(或某个内核)运行多进程会一直运行不出结果，所以用py脚本练习mulprocessing
# @Time    : 2021/5/29 15:23
# @Author  : songpeiyao
# @Version : 1.0
import multiprocessing as mp
import threading as td 

'''
def fetch_data_and_predict(num):
    print(num)


# 把数据分成5分，每次循环通过同一个方法中的参数，取不同的数据
p = None
for i in range(5):
    p = mp.Process(target=fetch_data_and_predict, args=(i,))
    p.start()
p.join()  # 等所有job运行完，才继续后面的步骤
'''

'''
# thread 和 mulprocessing 使用类似
def job(a,b):
    print('111')

t1 = td.Thread(target=job, args=(1,2))
t1.start()
t1.join()

p1 = mp.Process(target=job, args=(1,2))
p1.start()  # 开始
p1.join()  # 停止
'''

def job(q):
    res = 0 
    for i in range(10):
        res += i + i 
    q.put(res)

if __name__ == '__main__':
    q = mp.Queue()
    # todo 多个参数怎么传入 args
    p1 = mp.Process(target=job, args=(q,))  # 多进程的job不能有返回值，而是通过queue返回
    p2 = mp.Process(target=job, args=(q,))
    p1.start()  
    p2.start()
    p1.join()  
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1, res2)
