#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 01:05:04 2021

@author: jeff
"""

"""
Key Idea:
    Keep a monoqueue and pop from left
"""

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        P = [0]
        total = 0
        ans = float("inf")
        for num in nums:
            total += num
            P.append(total)
            
        queue = collections.deque()
        
        for y, Py in enumerate(P):
            while queue and Py <= P[queue[-1]]:
                queue.pop()
            while queue and Py - P[queue[0]] >= k:
                ans = min(ans, y - queue[0])
                queue.popleft()
            queue.append(y)
            
        return ans if ans != float("inf") else -1