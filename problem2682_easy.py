# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/8/16 9:26
"""
from typing import List

"""
n 个朋友在玩游戏。这些朋友坐成一个圈，按 顺时针方向 从 1 到 n 编号。从第 i 个朋友的位置开始顺时针移动 1 步会到达第 (i + 1) 个朋友的
位置（1 <= i < n），而从第 n 个朋友的位置开始顺时针移动 1 步会回到第 1 个朋友的位置。
游戏规则如下：
第 1 个朋友接球。
接着，第 1 个朋友将球传给距离他顺时针方向 k 步的朋友。
然后，接球的朋友应该把球传给距离他顺时针方向 2 * k 步的朋友。
接着，接球的朋友应该把球传给距离他顺时针方向 3 * k 步的朋友，以此类推。
换句话说，在第 i 轮中持有球的那位朋友需要将球传递给距离他顺时针方向 i * k 步的朋友。
当某个朋友第 2 次接到球时，游戏结束。
在整场游戏中没有接到过球的朋友是 输家 。
给你参与游戏的朋友数量 n 和一个整数 k ，请按升序排列返回包含所有输家编号的数组 answer 作为答案。

示例 1：
输入：n = 5, k = 2
输出：[4,5]
解释：以下为游戏进行情况：
1）第 1 个朋友接球，第 1 个朋友将球传给距离他顺时针方向 2 步的玩家 —— 第 3 个朋友。
2）第 3 个朋友将球传给距离他顺时针方向 4 步的玩家 —— 第 2 个朋友。
3）第 2 个朋友将球传给距离他顺时针方向 6 步的玩家 —— 第 3 个朋友。
4）第 3 个朋友接到两次球，游戏结束。

示例 2：
输入：n = 4, k = 4
输出：[2,3,4]
解释：以下为游戏进行情况：
1）第 1 个朋友接球，第 1 个朋友将球传给距离他顺时针方向 4 步的玩家 —— 第 1 个朋友。
2）第 1 个朋友接到两次球，游戏结束。
"""
"""
思路：直接模拟即可
"""


class Solution:
    @staticmethod
    def circularGameLosers(n: int, k: int) -> List[int]:
        cnt = [0] * n
        cnt[0] = 1
        time = 1
        now = 1
        while True:
            nxt = (now + time * k) % n
            cnt[nxt - 1] += 1
            if cnt[nxt - 1] == 2:
                break
            now = nxt
            time += 1
        ans = []
        for i in range(n):
            if cnt[i] == 0:
                ans.append(i + 1)
        return ans
