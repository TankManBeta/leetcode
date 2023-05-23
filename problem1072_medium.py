# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/15 9:44
"""
from collections import Counter
from typing import List

"""
给定 m x n 矩阵 matrix 。
你可以从中选出任意数量的列并翻转其上的 每个 单元格。（即翻转后，单元格的值从 0 变成 1，或者从 1 变为 0 。）
返回 经过一些翻转后，行与行之间所有值都相等的最大行数 。 

示例 1：
输入：matrix = [[0,1],[1,1]]
输出：1
解释：不进行翻转，有 1 行所有值都相等。

示例 2：
输入：matrix = [[0,1],[1,0]]
输出：2
解释：翻转第一列的值之后，这两行都由相等的值组成。

示例 3：
输入：matrix = [[0,0,0],[0,0,1],[1,1,0]]
输出：2
解释：翻转前两列的值之后，后两行由相等的值组成。
"""
"""
思路：我们观察发现，如果矩阵中的两行满足以下条件之一，则它们可以通过翻转某些列的方式得到相等的行：
    两行的对应位置元素相等，即如果其中一行元素为 1,0,0,1，则另一行元素也为 1,0,0,1；
    两行的对应位置元素相反，即如果其中一行元素为 1,0,0,1，则另一行元素为 0,1,1,0。
我们称满足以上条件之一的两行元素为“等价行”，那么题目所求的答案即为矩阵中最多包含等价行的行数。
因此，我们可以遍历矩阵的每一行，将每一行转换成第一个元素为 0 的“等价行”。具体做法如下：
    如果当前行的第一个元素为 0，那么当前行的元素保持不变；
    如果当前行的第一个元素为 1，那么我们将当前行的每个元素进行翻转，即 0 变成 1, 1 变成 0。也就是说，我们将以 1 开头的行翻转成以 
    0 开头的“等价行”。
这样一来，我们只需要用一个哈希表来统计转换后的每一行的出现次数，其中键为转换后的行（可以将所有数字拼接成一个字符串），值为该行
出现的次数。最后，哈希表中值的最大值即为矩阵中最多包含等价行的行数。
"""


class Solution:
    @staticmethod
    def maxEqualRowsAfterFlips(matrix: List[List[int]]) -> int:
        cnt = Counter()
        for row in matrix:
            t = tuple(row) if row[0] == 0 else tuple(x ^ 1 for x in row)
            cnt[t] += 1
        return max(cnt.values())