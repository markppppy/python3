#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : lgbm_eval_obj_by_f1.py
# @Desc    : 
# @Time    : 2021/8/3 9:44
# @Author  : songpeiyao
# @Version : 1.0

from typing import List

a = max(1, 2, 3)
# print(a) 

# print('%dA%dB'%(1, 2))

lst_origin = [3, 5, -1, 9, 12, 1]
lst_test = [-1, 2, 3, 4]
# 冒泡排序
def bubble_sort(lst: List):
    # 依次比较相邻元素，每次把最大的元素移到最后一位
    n = len(lst) 
    if n <= 1:
        return 
    for i in range(n-1):
        flag = True
        for l in range(n-1-i):
            if lst[l] > lst[l+1]:
                lst[l], lst[l+1] = lst[l+1], lst[l]
                flag = False 
        if flag:
            break
     

# 插入排序 
def insert_sort(lst: List):
    n = len(lst) 
    if n <= 1:
        return
    for i in range(n-1):
        j = i+1
        for l in range(j): 
            if lst[l] > lst[l+1]:
                lst[l], lst[l+1] = lst[l+1], lst[l]


# 选择排序
def selection_sort(lst: List):
    '''
    每次从未排序选择最小元素，和未排序子列表的第一个元素换位置
    '''
    n = len(lst)
    if n <= 1:
        return lst
    nsid = 0  # 未排序子列表的的第一个元素下标
    for l in range(n):  # 这个范围不重要，没那么精确 
        minid = nsid  # 最小元素下标 
        for i in range(nsid+1, n):
            if lst[i] < lst[minid]:
                minid = i 
        lst[minid], lst[nsid] = lst[nsid], lst[minid] 
        nsid += 1 

            



# selection_sort(lst_origin)
# selection_sort(lst_test)
# lst = insert_sort(lst_origin)

# 解决问题的方法和数据组织形式、空间利用率有关
def printN(n: int):
    if n:
        printN(n-1)
        print('%d'%n)

# printN(10)

str1 = {1,2,3}
str2 = {1,2}

print(str1 < str2)

x=3==3,5
print(x)

# 时间复杂度是log的算法

import sys 

target = [] 

for line in  sys.stdin:
    target.append(int(line))

