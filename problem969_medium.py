# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/19 16:43
"""
"""
给你一个整数数组 arr ，请使用 煎饼翻转 完成对数组的排序。
一次煎饼翻转的执行过程如下：
    选择一个整数 k ，1 <= k <= arr.length
    反转子数组 arr[0...k-1]（下标从 0 开始）
    例如，arr = [3,2,1,4] ，选择 k = 3 进行一次煎饼翻转，反转子数组 [3,2,1] ，得到 arr = [1,2,3,4] 。
以数组形式返回能使 arr 有序的煎饼翻转操作所对应的k值序列。
任何将数组排序且翻转次数在10*arr.length范围内的有效答案都将被判断为正确。

输入：[3,2,4,1]
输出：[4,2,4,3]
解释：
我们执行 4 次煎饼翻转，k 值分别为 4，2，4，和 3。
初始状态 arr = [3, 2, 4, 1]
第一次翻转后（k = 4）：arr = [1, 4, 2, 3]
第二次翻转后（k = 2）：arr = [4, 1, 2, 3]
第三次翻转后（k = 4）：arr = [3, 2, 1, 4]
第四次翻转后（k = 3）：arr = [1, 2, 3, 4]，此时已完成排序。 

输入：[1,2,3]
输出：[]
解释：
输入已经排序，因此不需要翻转任何内容。
请注意，其他可能的答案，如 [3，3] ，也将被判断为正确。
"""
"""
思路：每次翻转只会改变前面的，不会改变后面的，所以我们每次把最大的放后边即可
"""


class Solution(object):
    @staticmethod
    def pancake_sort(arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ans = []
        for n in range(len(arr), 1, -1):
            index = 0
            for i in range(n):
                if arr[i] > arr[index]:
                    index = i
            if index == n - 1:
                continue
            m = index
            for i in range((m + 1) // 2):
                arr[i], arr[m - i] = arr[m - i], arr[i]
            for i in range(n // 2):
                arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
            ans.append(index + 1)
            ans.append(n)
        return ans
