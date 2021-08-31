#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 16:33:01 2021

@author: jeff
"""

"""
Key Idea:
    Use BFS rather than DFS cause it use less memory.
"""

class Solution:
    def minDays(self, n: int) -> int:
        queue = collections.deque([n])
        visited = set()
        ans = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                number = queue.popleft()
                if number == 0 :
                    return ans
                if number % 3 == 0 and number/3 not in visited:
                    queue.append(number/3)
                    visited.add(number/3)
                if number % 2 == 0 and number/2 not in visited:
                    queue.append(number/2)
                    visited.add(number/2)
                if number - 1 not in visited:
                    queue.append(number-1)
                    visited.add(number-1)
            ans += 1