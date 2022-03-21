#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210610.py
# @Desc    : 
# @Time    : 2021/6/9 19:27
# @Author  : songpeiyao
# @Version : 1.0

"""
最长回文子串
https://leetcode-cn.com/leetbook/read/array-and-string/conm7/

给你一个字符串 s，找到 s 中最长的回文子串。

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

"""


def longestPalindrome(s: str) -> str:
    # 如果s[i..j]是回文串，那s[i+1..j-1]一定是回文串且s[i]==s[j]
    # 动态规划, 这道题理解能写出来，方法没有完全掌握
    n = len(s)
    if n < 2:
        return s
    max_len = 1
    begin = 0
    # dp[i][j] 表示 s[i..j] 是否是回文串
    dp = [[False] * n for _ in range(n)]  # shape [11,1] 1 -> [11]
    for i in range(n):  # 单个元素一定是回文串，如s[0]
        dp[i][i] = True
    # 递推开始
    # 先枚举子串长度, L=2,3,4,...n
    for L in range(2, n + 1):
        # 枚举左边界
        for i in range(n):
            # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
            j = L + i - 1
            # 如果右边界越界，就可以退出当前循环
            if j >= n:
                break
            if s[i] != s[j]:
                dp[i][j] = False
            else:  # s[i] == s[j]
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]  # 能保证dp[i + 1][j - 1]比dp[i][j]先遍历到吗? 能保证，因为是先遍历短的ij组合L
            # 只要 dp[i][j] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
            if dp[i][j] and j - i + 1 > max_len:
                max_len = j - i + 1
                begin = i
    return s[begin:begin + max_len]


if __name__ == '__main__':
    # s = "babad"
    # s = "ac"
    # s = "bb"
    s = "aacabdkacaa"
    print(longestPalindrome(s))
