# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/28 18:17
"""
from itertools import accumulate
from typing import List

"""
给定数组 nums 和一个整数 k 。我们将给定的数组 nums 分成 最多 k 个相邻的非空子数组 。 分数 由每个子数组内的平均值的总和构成。
注意我们必须使用 nums 数组中的每一个数进行分组，并且分数不一定需要是整数。
返回我们所能得到的最大 分数 是多少。答案误差在 10-6 内被视为是正确的。

示例 1:
输入: nums = [9,1,2,3,9], k = 3
输出: 20.00000
解释: 
nums 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20. 
我们也可以把 nums 分成[9, 1], [2], [3, 9]. 
这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.

示例 2:
输入: nums = [1,2,3,4,5,6,7], k = 4
输出: 20.50000
"""
"""
思路：动态规划，dp[i][j]表示把前i个分成j组的最大平均和，当 j = 1 时，dp[i][j] 是对应区间 [0,i−1] 的平均值；当 j > 1 时，
我们将可以将区间 [0,i-1] 分成 [0,x-1] 和 [x,i-1] 两个部分，其中 x≥j−1，那么 dp[i][j] 等于所有这些合法的切分方式的平均值和的最大值。
"""


class Solution:
    @staticmethod
    def largestSumOfAverages(nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = list(accumulate(nums, initial=0))
        dp = [[0.0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][1] = prefix[i] / i
        for j in range(2, k + 1):
            for i in range(j, n + 1):
                for x in range(j - 1, i):
                    dp[i][j] = max(dp[i][j], dp[x][j - 1] + (prefix[i] - prefix[x]) / (i - x))
        return dp[n][k]