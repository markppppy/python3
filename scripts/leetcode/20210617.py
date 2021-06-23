#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210617.py
# @Desc    : 
# @Time    : 2021/6/17 10:29
# @Author  : songpeiyao
# @Version : 1.0
"""
实现 strStr()

给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回 -1 。

说明：
当needle是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当needle是空字符串时我们应当返回 0 。这与 C 语言的strstr()以及 Java 的indexOf()定义相符。
haystack 和 needle 仅由小写英文字符组成

输入：haystack = "hello", needle = "ll"
输出：2
"""


def strStr(haystack: str, needle: str) -> int:
    # 使用kmp算法，这里的写法有待优化;
    # i haystack  j needle
    ln_needle = len(needle)
    if ln_needle == 0:
        return 0
    ln = len(haystack)
    for n in range(ln):
        if haystack[n] == needle[0]:
            if ln - n + 1 < ln_needle:
                return -1
            for j in range(ln_needle):
                if n+j > ln - 1 or needle[j] != haystack[n+j]:  # aaa 和 aaaa 特殊情况的考虑 n+j > ln - 1
                    break
                if j == ln_needle - 1:
                    return n
    return -1


if __name__ == '__main__':
    # haystack = "hello"
    # needle = "ll"
    haystack = "aaa"
    needle = "aaaa"
    print(strStr(haystack, needle))

