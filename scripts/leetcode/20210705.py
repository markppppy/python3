#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210705.py
# @Desc    : 
# @Time    : 2021/7/5 19:28
# @Author  : songpeiyao
# @Version : 1.0

"""
726. 原子的数量
给定一个化学式formula（作为字符串），返回每种原子的数量。

原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。

如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。

两个化学式连在一起是新的化学式。例如H2O2He3Mg4 也是化学式。

一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。

给定一个化学式formula ，返回所有原子的数量。格式为：第一个（按字典序）原子的名字，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。


输入：formula = "K4(ON(SO3)2)2"
输出："K4N2O14S4"
解释：
原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。

"""
from collections import defaultdict, deque


def countOfAtoms(formula: str) -> str:
    n = len(formula)
    map = defaultdict(lambda: 1)  # lambda: 1   ?
    d = deque([])  # deque 双向队列 [] 指定为列表
    i = idx = 0  # i formula的索引, idx ?
    while i < n:
        c = formula[i]
        if c == '(' or c == ')':
            d.append(c)
            i += 1
        else:
            if str.isdigit(c):
                # 获取完整的数字长度
                j = i
                while j < n and str.isdigit(formula[j]):
                    j += 1
                cnt = int(formula[i:j])
                i = j
                # 如果栈顶元素是 ) , 说明当前数值可以给一段 原子
                if d and d[-1] == ')':
                    tmp = []
                    d.pop()
                    while d and d[-1] != '(':
                        cur = d.pop()
                        map[cur] *= cnt
                        tmp.append(cur)
                    d.pop()

                    for k in range(len(tmp)-1, -1, -1):
                        d.append(tmp[k])
                else:
                    cur = d.pop()
                    map[cur] *= cnt
                    d.append(cur)
            else:
                # 获取完整的原子名
                j = i + 1
                while j < n and str.islower(formula[j]):
                    j += 1
                cur = formula[i:j] + "_" + str(idx)
                idx += 1
                map[cur] = 1
                i = j
                d.append(cur)
    # 将不同编号的相同原子进行合并
    mm = defaultdict(int)
    for key, cnt in map.items():
        atom = key.split("_")[0]
        mm[atom] += cnt

    # 对mm中的key进行排序作为答案
    ans = []
    for key in sorted(mm.keys()):
        if mm[key] > 1:
            ans.append(key+str(mm[key]))
        else:
            ans.append(key)
    return "".join(ans)


if __name__ == '__main__':
    formula = "K4(ON(SO3)2)2"  # "K4N2O14S4"
    print(countOfAtoms(formula))


