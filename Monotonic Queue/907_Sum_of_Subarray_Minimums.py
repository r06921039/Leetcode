#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 17:25:11 2021

@author: jeff
"""

"""
Key Idea:
    Find prev less index and next less index
    left[i] = i - prev_less_index
    right[i] = next_less_index - i
    And the ans will add arr[i]*left[i]*right[i]
"""
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = n * [0]
        right = [n - i for i in range(n)]
        stack_prev = []
        stack_next = []
        ans = 0
        for i in range(n):
            # find prev less
            while stack_prev and stack_prev[-1][0] > arr[i]:
                stack_prev.pop()
            left[i] = i - stack_prev[-1][1]  if stack_prev else i+1
            stack_prev.append([arr[i], i])
            # find next less
            while stack_next and stack_next[-1][0] > arr[i]:
                curr = stack_next.pop()
                right[curr[1]] = i - curr[1]
            stack_next.append([arr[i], i])
        
        for i in range(n):
            ans += arr[i] * left[i] * right[i]
            
        return ans % 1_000_000_007