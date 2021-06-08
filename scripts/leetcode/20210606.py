"""
5776. 判断矩阵经轮转后是否一致
给你两个大小为 n x n 的二进制矩阵 mat 和 target 。现 以 90 度顺时针轮转 矩阵 mat 中的元素 若干次 ，如果能够使 mat 与 target 一致，返回 true ；否则，返回 false 。

"""
from typing import List


def findRotation(mat: List[List[int]], target: List[List[int]]) -> bool:
    # 转一个90°，两个90是上下翻转，3个90都是逆时针90，4个90是相等
    # 判断两个矩阵是否同构
    #1、判断两个矩阵是否相等
    if mat == target:
        return True
    # 2、上下翻转
    n = len(mat)
    i = 0
    j = 0
    _mat = [[mat[a][b] for b in range(len(mat[0]))] for a in range(len(mat))]  # 列表复制; 直接等号或lst[:]是引用拷贝
    while i < n//2:
        for j in range(n):
            _mat[i][j], _mat[n-i-1][j] = _mat[n-i-1][j], _mat[i][j]
        i += 1
    if _mat == target:
        return True
    _mat_1 = [[_mat[a][b] for b in range(len(_mat[0]))] for a in range(len(_mat))]
    # 3、顺时针90，即主对角线交换
    for i in range(n):
        for b in range(i):
            _mat_1[i][b], _mat_1[b][i] = _mat_1[b][i], _mat_1[i][b]
    if _mat_1 == target:
        return True
    # 4、逆时针90，即副对角线交换
    a = n-1
    while a >= 0:
        for j in range(a):
            if a + j != n:
                _mat[a][j], _mat[j][n-a-1] = _mat[j][n-a-1], _mat[a][j]
        a -= 1
    if _mat == target:
        return True
    return False


if __name__ == '__main__':
    mat = [[0, 1], [1, 1]]
    target = [[1, 0], [0, 1]]
    # mat = [[0, 1], [1, 0]]
    # target = [[1, 0], [0, 1]]
    print(findRotation(mat, target))
    print()
