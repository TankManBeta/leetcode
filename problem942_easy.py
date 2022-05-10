# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/5/9 11:42
"""
"""
由范围 [0,n] 内所有整数组成的 n + 1 个整数的排列序列可以表示为长度为 n 的字符串 s ，其中:
如果 perm[i] < perm[i + 1] ，那么 s[i] == 'I' 
如果 perm[i] > perm[i + 1] ，那么 s[i] == 'D' 
给定一个字符串 s ，重构排列 perm 并返回它。如果有多个有效排列perm，则返回其中 任何一个 。

输入：s = "IDID"
输出：[0,4,1,3,2]

输入：s = "III"
输出：[0,1,2,3]

输入：s = "DDI"
输出：[3,2,0,1]
"""
"""
思路：贪心，如果是D就把当前这个位置给最大的，如果是I就把当前这个位置给最小的
"""


class Solution(object):
    @staticmethod
    def diStringMatch(s):
        """
        :type s: str
        :rtype: List[int]
        """
        lo = 0
        hi = n = len(s)
        perm = [0] * (n + 1)
        for i, ch in enumerate(s):
            if ch == 'I':
                perm[i] = lo
                lo += 1
            else:
                perm[i] = hi
                hi -= 1
        perm[n] = lo
        return perm
