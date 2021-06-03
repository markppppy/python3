#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210603.py
# @Desc    : 
# @Time    : 2021/6/3 18:48
# @Author  : songpeiyao
# @Version : 1.0
from typing import List
"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/array-and-string/c5tv3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    感想：自己没想出来，看了别人的思路，复现的；
    :param intervals:
    :return:
    """
    # 把数组按照子数组的第一位排序
    intervals.sort(key=lambda x: x[0])
    target = []
    for n in intervals:
        if not target or target[-1][-1] < n[0]:
            target.append(n)
        else:
            target[-1][-1] = max(n[-1], target[-1][-1])  # 合并

    return target


input_lst = [[1, 4], [0, 2], [3, 5]]
print(merge(input_lst))


