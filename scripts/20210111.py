#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @File    : 20210111.py
# @Desc    : 
# @Time    : 2021/01/11 22:05:03
# @Author  : songpeiyao
# @Version : 1.0

# 程序逻辑构造

# 寻找水仙花数：一个三位数，满足条件：每个位置上的数字立方和等于数字本身
def get_appoint_num(start_num: int, end_num: int): 
    nums = []
    for num in range(start_num, end_num):
        low = num % 10 
        middle = num // 10 % 10
        high = num // 100 % 10
        if num == low ** 3 + middle** 3 + high ** 3:
            nums.append(num)
    return nums

# 反转整数：12345变成54321
def get_reversed_int():
    num = int(input('num = '))
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num = num // 10
    print(reversed_num)

"""
Craps游戏：
玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；
其他点数，玩家继续要骰子，直到分出胜负
"""
from random import randint

def do_craps():
    money = 1000
    while money > 0:
        print('你的资产为：', money)
        needs_go_on = False
        while True:
            debt = int(input('请下注：'))
            if 0 < debt <= money:
                break
        first = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % first)
        if first == 7 or first == 11:
            print('玩家胜!')
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print('庄家胜!')
            money -= debt
        else:
            needs_go_on = True 
        while needs_go_on:
            needs_go_on = False
            current = randint(1, 6) + randint(1, 6)
            print('玩家摇出了%d点' % current)
            if current == 7:
                print('庄家胜!')
                money -= debt
            elif current == first:
                print('玩家胜!')
                money += debt
            else:
                needs_go_on = True
    print('你破产了，游戏结束!')

if __name__ == "__main__":
    # print(get_appoint_num(210, 800))
    # get_reversed_int()
    do_craps()

