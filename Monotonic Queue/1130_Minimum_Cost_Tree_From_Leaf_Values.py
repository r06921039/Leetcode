#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 23:52:59 2021

@author: jeff
"""

"""
Key Idea:
    1. Use DP and create helper to recursive from top to bottom complexity O(n^3)
    2. Use Monotonic stack
    
"""

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        memo = {}
        
        def helper(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if left >= right:
                return 0
            
            res = float("inf")
            
            for i in range(left, right):
                rootValue = max(arr[left:i+1]) * max(arr[i+1:right+1])
                res = min(res, helper(left, i) + helper(i+1, right) + rootValue)
            
            memo[(left, right)] = res
            return res
                
            
        return helper(0, len(arr) - 1)
    



class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float("inf")]
        ans = 0
        for num in arr:
            while num >= stack[-1]:
                curr = stack.pop()
                ans += curr * min(stack[-1], num)
            stack.append(num)
        while len(stack) > 2:
            ans += stack.pop() * stack[-1]
            
        return ans