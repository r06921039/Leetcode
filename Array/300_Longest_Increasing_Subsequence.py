#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 21:50:38 2021

@author: jeff
"""

"""
Key Idea:
    Keep a tail to record last element
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [float("-inf")] * len(nums)
        size = 0
        for num in nums:
            low = 0
            high = size
            while low < high:
                mid = (low + high) // 2
                if tails[mid] < num:
                    low = mid + 1
                else:
                    high = mid
            
            tails[low] = num
            size = max(size, low+1)
            
        return size