#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 00:29:45 2021

@author: jeff
"""

"""
Key Idea:
    Using running sum and keep a left pointer
    if running sum reach the goal then start moving left pointer
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        ans = float("inf")
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                ans = min(ans, i - left + 1)
                total -= nums[left]
                left += 1
        
        return ans if ans != float("inf") else 0