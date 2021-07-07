#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210707.py
# @Desc    : 
# @Time    : 2021/7/7 19:13
# @Author  : songpeiyao
# @Version : 1.0
"""
1711. 大餐计数

大餐 是指 恰好包含两道不同餐品 的一餐，其美味程度之和等于 2 的幂。

你可以搭配 任意 两道餐品做一顿大餐。

给你一个整数数组 deliciousness ，其中 deliciousness[i] 是第 i道餐品的美味程度，返回你可以用数组中的餐品做出的不同 大餐 的数量。结果需要对 10**9 + 7 取余。

注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。


输入：deliciousness = [1,3,5,7,9]
输出：4
解释：大餐的美味程度组合为 (1,3) 、(1,7) 、(3,5) 和 (7,9) 。
它们各自的美味程度之和分别为 4 、8 、8 和 16 ，都是 2 的幂。

题目释义：返回的是不同大餐的数量；大餐是指2个不同索引数字和为2的幂的组合；
结果需要对 10**9 + 7 取余。 ???  怕超过什么限制?
"""
from typing import List


def countPairs(deliciousness: List[int]) -> int:
    # 思路: 双指针，遍历所有两两组合；
    # 怎么判断和为2的幂? 只要数字n和n-1的位与运算为0，n就是2的幂
    def judge(num):
        return True if num & (num-1) == 0 else False
    i = 0
    n = len(deliciousness)
    cnt = 0
    while i < n-1:
        for j in range(i+1, n):
            if judge(deliciousness[i]+deliciousness[j]):
                print(i, deliciousness[i], j, deliciousness[j])
                cnt += 1
        i += 1
    return cnt % (10**9+7)


if __name__ == '__main__':
    deliciousness = [2160, 1936, 3, 29, 27, 5, 2503, 1593, 2, 0, 16, 0, 3860, 28908, 6, 2, 15, 49, 6246, 1946, 23, 105,
                     7996, 196, 0, 2, 55, 457, 5, 3, 924, 7268, 16, 48, 4, 0, 12, 116, 2628, 1468]
    print(countPairs(deliciousness))





