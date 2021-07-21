#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:43:16 2021

@author: jeff
"""
import collections

"""

Key Idea:
atMost(k) - atMost(k-1) equals exact k

"""

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atMost(k):
            table = collections.defaultdict(int)
            left = 0
            ans = 0
            for right, num in enumerate(nums):
                table[num] += 1
                while len(table) > k:
                    table[nums[left]] -= 1
                    if table[nums[left]] == 0:
                        del table[nums[left]]
                    left += 1
                ans += right - left + 1
            return ans
        
        return atMost(k) - atMost(k-1)