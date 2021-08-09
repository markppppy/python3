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
        for i in range(srtd+1, n):
            if lst[i] < lst[min_index]:
                min_index = i
        lst[srtd], lst[min_index] = lst[min_index], lst[srtd]
        srtd += 1
    return lst


def quick_sort(arr, low, high):
    # 快速排序: 选取基准值，把所有比他小的元素放在前面，比他大的放在后面；然后再在前后两个集合中重复这个操作，直到集合中的元素个数为0或为1；
    # 递归执行条件 low < high
    if low < high:
        # 选取基准值，并把集合按照基准值划分
        pi = partition(arr, low, high)
        # 对子集合进行递归
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, low)


def partition(arr, low, high):
    i = low - 1  # 定义最小索引
    pivot = arr[high]  # 基准值
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1  # 返回基准值对应的下标


# 每次把 arr[low, high]中 小于 pivot的元素放前面，大于 pivot 的元素放后面
def partition_(arr, low, high):
    i = (low - 1)  # 最小元素索引  i 前面的都是小于 pivot的， 最后把 i+1的元素和 po
    pivot = arr[high]
    for j in range(low, high):  # 这个遍历不到 arr[high]
        # 当前元素小于或等于 pivot 
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序
def quickSort(arr, low, high):
    if low < high:
        pi = partition_(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


if __name__ == '__main__':
    lst_origin = [3, 5, -1, 9, 12, 1]
    # print(selection_sort(lst_origin))
    n = len(lst_origin)-1
    # quickSort(lst_origin, 0, n)
    quick_sort(lst_origin, 0, n)
    print(lst_origin)
    # for i in range(0):  # 不会循环的
    #     print('wulawula')

    # lst1 = [1, 2, 3]
    # lst2 = [3, 5]
    # a = 0
    # print(lst1 + lst2 + [a])

