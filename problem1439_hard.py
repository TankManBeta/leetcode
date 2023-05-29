# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/28 14:00
"""
from typing import List

"""
给你一个 m * n 的矩阵 mat，以及一个整数 k ，矩阵中的每一行都以非递减的顺序排列。
你可以从每一行中选出 1 个元素形成一个数组。返回所有可能数组中的第 k 个 最小 数组和。 

示例 1：
输入：mat = [[1,3,11],[2,4,6]], k = 5
输出：7
解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
[1,2], [1,4], [3,2], [3,4], [1,6]。其中第 5 个的和是 7 。  

示例 2：
输入：mat = [[1,3,11],[2,4,6]], k = 9
输出：17

示例 3：
输入：mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
输出：9
解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]。其中第 7 个的和是 9 。 

示例 4：
输入：mat = [[1,1,10],[2,2,9]], k = 7
输出：12
"""
"""
思路：如果我们能够找出前 m−1 行的所有可能数组中的前 k 个最小数组和，那么我们可以将第 m 行的每个元素与前 m−1 行的前 k 个最小
数组和相加，将得到的所有结果排序后，取前 k 个最小值，即为前 m 行的所有可能数组中的前 k 个最小值。因此，我们可以定义一个数组 pre，
用于存储此前遍历到的行的前 k 个最小数组和，初始时 pre 只有一个元素 0。然后，我们遍历 mat 的每一行 cur，将 cur 中的每个元素与 
pre 中的每个元素相加，将得到的所有结果排序后，取前 k 个最小值作为新的 pre。继续遍历下一行，直到遍历完所有行。最后返回 pre 中的
第 k 个数（下标 k−1）即可。
"""


class Solution:
    @staticmethod
    def kthSmallest(mat: List[List[int]], k: int) -> int:
        pre = [0]
        for cur in mat:
            pre = sorted(a + b for a in pre for b in cur[:k])[:k]
        return pre[-1]
