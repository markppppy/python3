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
# 冒泡排序
def bubble_sort(lst: List):
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(n-1):  # 循环的次数
        flag = True  # 如果已经有序，终止循环
        for l in range(n-i-1):
            if lst[l] > lst[l+1]:
                lst[l], lst[l+1] = lst[l+1], lst[l] 
                flag = False
        if flag:
            break 
    return lst 

# 插入排序 
def insert_sort(lst: List):
    n = len(lst) 
    if n <= 1:
        return lst 
    # for i in range(n-1): # 循环的次数，每次循环从后面拿一个元素
    #     for l in range(i+1): # 用拿到的元素和前面已有序的元素依次比较
    #         if lst[i+1] < lst[l]:
    #             lst[i+1], lst[l] = lst[l], lst[i+1]
    for i in range(n-1): # 循环的次数，每次循环从后面拿一个元素
        key = lst[i+1]
        j = i 
        while j >= 0 and key <= lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key    
    return lst             

# print(insert_sort(lst_origin))



