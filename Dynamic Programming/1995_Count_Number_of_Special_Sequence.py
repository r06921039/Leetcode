#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 23:08:23 2021

@author: jeff
"""

"""
Key Idea:
    keep track on number of seq 0, seq 1 and seq 2
    So everytime encounter a new number
    0: dp[0] += dp[0] + 1
    1: dp[1] += dp[1] + dp[0]
    2: dp[2] += dp[2] + dp[1]
"""

class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        dp = [1, 0, 0, 0]
        for num in nums:
            dp[num+1] += (dp[num] + dp[num+1])
        return dp[-1] % 1_000_000_007