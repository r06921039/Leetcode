#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 22:18:54 2021

@author: jeff
"""

"""
Key Idea:
    Use BFS but remeber to clear the table when you have visited
"""

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        
        table = {}
        
        for i, num in enumerate(arr):
            if num not in table:
                table[num] = [i]
            else:
                table[num].append(i)
        
        queue = collections.deque([0])
        jumps = 0
        visited = set()
        
        while queue:
            size = len(queue)
            for _ in range(size):
                i = queue.popleft()
                visited.add(i)
                if i == len(arr) - 1:
                    return jumps
                for next_pos in [i+1] + [i-1] + table[arr[i]]:
                    if 0 <= next_pos < len(arr) and next_pos not in visited:
                        queue.append(next_pos)
                table[arr[i]].clear()
            jumps += 1
            
        return jumps