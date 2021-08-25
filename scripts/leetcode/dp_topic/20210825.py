#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210825.py
# @Desc    : 
# @Time    : 2021/8/25 17:16
# @Author  : songpeiyao
# @Version : 1.0
"""
70. 爬楼梯

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

746. 使用最小花费爬楼梯

数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值cost[i]（下标从 0 开始）。
每当你爬上一个阶梯你都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。
请你找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。

题目释义: 可以选择站在cost的下标0或1的位置开始，每次前进只要支付了所在楼梯的值可以选择走一步或两步。
"""
from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        # todo 递归，记忆化递归，动态规划； 其中记忆化递归还没实现
        # 在走完楼梯前，1和2有多少种组合
        # 可以用递归和动态规划
        # 递归公式: f(n) = f(n-1) + f(n-2) # 到达楼顶的最后一步可能是1步, 也可能是2步; f(1) = 1, f(2) = 2; 终止条件: n <= 2
        # if n > 2:
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)
        # elif n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # 动态规划: n=1,1; n=2,2; n=3,3; n=4,5; n=5,8... 有点像斐波那契数列
        p, q, r = None, None, None  # p 是走到前1阶可能的组合数，q 是走到前2阶可能的组合数，r 是走到当前台阶的可能组合数
        for i in range(1, n+1):
            if i == 1:
                p = 1
                r = 1
            elif i == 2:
                q = 1
                p = 2
                r = 2
            else:  # 这个实现就是滚动数组思想吧
                r = p + q
                p, q = r, p

        return r

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 第一步是比较 起始点和下两步的cost还是只比较起始步的cost? 后面的每一步呢?  题目中的思路是计算所有可能到该点的最小代价，而不是下一步怎么走代价最小
        # 创建n+1的数组，dp[i]表示到i时的最小代价，dp[0]=dp[1]=0
        n = len(cost)
        # dp = [0] * (n+1)
        # for i in range(2, n+1):
        #     dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        # return dp[n]
        # method 1 over
        # 滚动数组
        prev = curr = 0
        for i in range(2, n+1):
            nxt = min(prev+cost[i-2], curr+cost[i-1])
            prev, curr = curr, nxt
        return curr


if __name__ == '__main__':
    print()