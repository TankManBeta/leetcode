# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/19 0:09
"""
"""
给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。
两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：
    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
注意：a + b 意味着字符串 a 和 b 连接。

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false

输入：s1 = "", s2 = "", s3 = ""
输出：true
"""
"""
思路：直接dp，dp[i][j]是s1前i个和s2前j个能否构成s3[i+j]，dp[i][j]为前面能否匹配成功与上当前是否匹配成功
"""


class Solution(object):
    @staticmethod
    def is_interleave(s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if len1+len2 != len3:
            return False
        dp = [[False]*(len2+1) for _ in range(len1+1)]
        dp[0][0] = True
        for i in range(1, len1+1):
            dp[i][0] = (dp[i-1][0] and s1[i-1] == s3[i-1])
        for i in range(1, len2+1):
            dp[0][i] = (dp[0][i-1] and s2[i-1] == s3[i-1])
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                dp[i][j] = (dp[i][j-1] and s2[j-1] == s3[i+j-1]) or (dp[i-1][j] and s1[i-1] == s3[i+j-1])
        return dp[-1][-1]
