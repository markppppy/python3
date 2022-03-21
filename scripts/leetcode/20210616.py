#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210616.py
# @Desc    : 
# @Time    : 2021/6/16 9:48
# @Author  : songpeiyao
# @Version : 1.0
"""
翻转字符串里的单词

给你一个字符串 s ，逐个翻转字符串中的所有 单词 。

单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。

请你返回一个翻转 s 中单词顺序并用单个空格相连的字符串。

说明：

输入字符串 s 可以在前面、后面或者单词间包含多余的空格。
翻转后单词间应当仅用一个空格分隔。
翻转后的字符串中不应包含额外的空格。


输入：s = "the sky is blue"
输出："blue is sky the"
"""


def reverseWords(s: str) -> str:
    b = None
    n = len(s)
    for i in range(n):
        if s[i] != ' ':
            b = i
            break
    if b is None:
        return s
    word = ''
    lst = []
    for i in range(b, n):
        if s[i] != ' ' and i != n-1:  # i != s[-1] the == blue ?
            word += s[i]
        elif i == n-1 and s[i] != ' ':
            word += s[i]
            lst.insert(0, word)
            break
        else:
            if word != '':
                lst.insert(0, word)
            word = ''

    return ' '.join(lst)


if __name__ == '__main__':
    # s1 = "the sky is blue"
    # s2 = reverseWords(s1)
    s1 = "  hello world  "
    s2 = reverseWords(s1)
    print(s2)
