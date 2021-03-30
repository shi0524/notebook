#! --*-- coding: utf-8 --*--

"""
74. 搜索二维矩阵

难度: 中等

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

示例:
    输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    输出：true

    输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    输出：false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
"""


# 每行遍历, 确定行, 遍历列, 确定列  L 型遍历
def searchMatrix_01(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    m = len(matrix)
    n = len(matrix[0])
    x = m-1
    y = 0
    while x >-1 and y < n:
        if matrix[x][y] == target:
            return True
        elif matrix[x][y] > target:
            x = x-1
        else:
            y = y+1
    return False


# 二分查确定行, 再二分查找确定列
def searchMatrix_02(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    col_index = search_column(matrix, target)
    if 0 <= col_index < len(matrix):
        return search_row(matrix[col_index], target)
    return False


def search_column(matrix, target):
    N = len(matrix)
    L = 0
    R = N-1
    mid = (L + N)/2
    while L < R:
        if matrix[mid][0] <= target <= matrix[mid][-1]:
            return mid
        elif matrix[mid][0] < target:
            L = mid + 1
        else:
            R = mid - 1
        mid = (L + R) / 2
    return mid


def search_row(lst, target):
    N = len(lst)
    L = 0
    R = N-1
    mid = (L + R) / 2
    while L <= R:
        if lst[mid] < target:
            L = mid + 1
        elif lst[mid] > target:
            R = mid - 1
        else:
            return True
        mid = (L + R) / 2
    return False


# 想象中, 将二维数组拉平成一维数组, 用二分查找查询, 将一维索引 再 对应回二维数组坐标
def searchMatrix_03(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    # 二分查找
    N = len(matrix)
    M = len(matrix[0])
    L = 0
    R = M * N - 1
    while L <= R:
        mid = (L + R) / 2
        num = matrix[mid / M][mid % M]
        if num == target:
            return True
        elif num < target:
            L = mid + 1
        else:
            R = mid - 1
    return False

if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3

    print searchMatrix_01(matrix, target)
    print searchMatrix_02(matrix, target)
    print searchMatrix_03(matrix, target)
