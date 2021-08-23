#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 21:35:02 2021

@author: jeff
"""

"""
Key Idea:
    Keep track on the farthest index that can be reach
    while current_jump_end reaches, current_jump_end = farthest and jumps += 1
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        jumps = 0
        current_jump_end = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest
        
        return jumps