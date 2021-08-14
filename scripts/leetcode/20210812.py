"""
最长回文子序列

给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。

acfvfsvaca

s 仅由小写英文字母组成

# 动态规划： 完全超出知识范畴....
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 标记每个字符，如果一个字符出现两次，则有一个长度为3的回文子串
        # 如果有两个字符出现两次，且顺序相反或字符相等，则有 2*2+1个回文子串
        # 对撞指针
        n = len(s)
        i = 0
        max_sub = 0
        for i in range(0, n):
            for j in range(1, n):
                if i < j:
                    if s[i] == s[-j]:
                        max_sub += 1
                        i += 1
                        j += 1



