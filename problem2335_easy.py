# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/11 14:40
"""
from typing import List

"""
现有一台饮水机，可以制备冷水、温水和热水。每秒钟，可以装满 2 杯 不同 类型的水或者 1 杯任意类型的水。
给你一个下标从 0 开始、长度为 3 的整数数组 amount ，其中 amount[0]、amount[1] 和 amount[2] 分别表示需要装满冷水、温水和
热水的杯子数量。返回装满所有杯子所需的 最少 秒数。

示例 1：
输入：amount = [1,4,2]
输出：4
解释：下面给出一种方案：
第 1 秒：装满一杯冷水和一杯温水。
第 2 秒：装满一杯温水和一杯热水。
第 3 秒：装满一杯温水和一杯热水。
第 4 秒：装满一杯温水。
可以证明最少需要 4 秒才能装满所有杯子。

示例 2：
输入：amount = [5,4,4]
输出：7
解释：下面给出一种方案：
第 1 秒：装满一杯冷水和一杯热水。
第 2 秒：装满一杯冷水和一杯温水。
第 3 秒：装满一杯冷水和一杯温水。
第 4 秒：装满一杯温水和一杯热水。
第 5 秒：装满一杯冷水和一杯热水。
第 6 秒：装满一杯冷水和一杯温水。
第 7 秒：装满一杯热水。

示例 3：
输入：amount = [5,0,0]
输出：5
解释：每秒装满一杯冷水。
"""
"""
思路：
（1）贪心+排序。每次选择两个最大的数进行减一操作，直到全都为0即可。
（2）贪心+分类讨论。设a≤b≤c，如果a+b≤c，则说明只需要c次即可全部减为0；若a+b>c，则每次可以使得两个数减一，最终匹配完或者剩下最后
一个数（取决于总和是偶数还是奇数），因此答案为 ⌊(a+b+c+1)/2⌋。
"""


class Solution:
    @staticmethod
    def fillCups(amount: List[int]) -> int:
        # ans = 0
        # while sum(amount):
        #     amount.sort()
        #     ans += 1
        #     amount[2] -= 1
        #     amount[1] = max(0, amount[1] - 1)
        # return ans

        amount.sort()
        if amount[0] + amount[1] <= amount[2]:
            return amount[2]
        return (sum(amount) + 1) // 2