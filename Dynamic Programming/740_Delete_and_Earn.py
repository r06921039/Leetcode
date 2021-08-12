#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 21:51:28 2021

@author: jeff
"""

"""

Key Idea:
    Turn the nums to points and use the same method as 198. House Robber
    
"""

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        r = max(nums)
        points = [0] * (r+1)
        for num in nums:
            points[num] += num
        
        dp1 = 0
        dp2 = 0
        for i in range(r+1):
            dp = max(dp1, dp2 + points[i])
            dp2 = dp1
            dp1 = dp
        
        return dp