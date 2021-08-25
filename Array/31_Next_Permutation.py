#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 22:06:18 2021

@author: jeff
"""

"""
Key Idea:
    Iterate from the right and find a[i] > a[i-1]
    Then find a[j] which is slight bigger than a[i-1] and swap
    reverse a[i:]
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums)-1, -1, -1):
            if i >= 1 and nums[i] > nums[i-1]:
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        break
                break
        nums[i:] = nums[i:][::-1]
        
        return nums