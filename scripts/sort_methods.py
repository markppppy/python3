#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : sort_methods.py
# @Desc    : 
# @Time    : 2021/6/2 17:20
# @Author  : songpeiyao
# @Version : 1.0

"""
各种排序算法和实现

冒泡排序: 交换;
插入排序: 插入;
选择排序: 插入;
希尔排序: 插入;
桶排序: 插入;
快速排序: 分治法;
归并排序: 分治法;
基数排序: 先比较个位数字, 排序; 然后比较十位数字, 排序...;
堆排序:
二叉排序树:
睡排序
猴子排序

衡量一个排序算法的好坏可以从3个方面来看: 执行效率(最好、最坏、平均时间复杂度)、占用内存(空间复制度)、稳定性(同样大小的元素在排序前后位置关系会不会变化)；
"""
from typing import List


def buble_sort(lst: List) -> List:
    # 冒泡排序，每次比较相邻元素，如果前面的大于后面的，就交换位置，每次会把未排序元素中最大元素换到后面
    # 优化: 如果有一次冒泡的过程中，没有元素交换，那证明当前元素已经是有序的了, 跳过后面的比较。可以用 flag 来实现。
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(n):  # 遍历的次数，和元素位置没关系
        flag = True
        for j in range(n-i-1):  # 每次遍历会把有序元素放在最后，所以只比较前面的元素; 为什么是 n-i-1 ? i 是从0开始, 当 i=0 时, n-1即lst的最后一个元素就不用遍历了, 因为 j, j+1
            if lst[j] > lst[j+1]:  # 这里是大于号, 所以这个冒泡排序是稳定的
                lst[j], lst[j+1] = lst[j+1], lst[j]
                flag = False
        if flag:
            break
    return lst


def insert_sort(lst: List) -> List:
    # 插入排序，每次从后面未排序的元素中，取一个，和前面已排序的元素对比
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(1, n):  # 每次从 i 到 n-1 取一个元素
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:  # 要把元素 lst[i] 插入到 i前合适的位置;  key < lst[j] 决定了结果从小到大还是从大到小, 这个我没想到
            # 如果 key 小于 lst[j]， 把 lst[j]往后移一位
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst


def selection_sort(lst: List) -> List:
    # 选择排序，每次从未排序的元素中取出最小元素，放在已排序元素列表的末尾(即: 和未排序元素列表中的第一个元素交换位置)
    # 3个时间复杂度都是O(n^2) 非稳定性排序
    n = len(lst)
    if n <= 1:
        return lst
    srtd = 0  # 索引，是未排序列表的位置，用来维护已排序列表
    while srtd < n:
        min_index = srtd
        for i in range(srtd, n):
            if lst[i] < lst[min_index]:
                min_index = i
        lst[srtd], lst[min_index] = lst[min_index], lst[srtd]
        srtd += 1
    return lst


if __name__ == '__main__':
    lst_origin = [3, 5, 1, 9, 12, -1]
    print(selection_sort(lst_origin))
    # for i in range(0):  # 不会循环的
    #     print('wulawula')
