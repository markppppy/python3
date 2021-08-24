#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210824.py
# @Desc    : 
# @Time    : 2021/8/24 18:43
# @Author  : songpeiyao
# @Version : 1.0

"""
509. 斐波那契数  fib

斐波那契数，通常用F(n) 表示，形成的序列称为 斐波那契数列 。该数列由0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1)= 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给你 n ，请计算 F(n) 。

1137. 第 N 个泰波那契数  tribonacci

泰波那契序列Tn定义如下：

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数n，请返回第 n 个泰波那契数Tn 的值。

"""


class Solution:
    def fib(self, n: int) -> int:
        # 递归: 终止条件: n = 0 or n = 1
        if n >= 2:
            return self.fib(n-1) + self.fib(n-2)
        elif n == 1:
            return 1
        elif n == 0:
            return 0

    def tribonacci(self, n: int) -> int:
        # 同上思路可以，但是会超时，必须使用动态规划或其他更优解法
        # 1、动态规划
        # 边界条件
        if n == 0:
            return 0
        if n <= 2:
            return 1
        # 核心: 每次往后移1位
        p = 0
        q = r = 1
        for i in range(3, n+1):
            s = p + q + r
            p, q, r = q, r, s
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.fib(4))
