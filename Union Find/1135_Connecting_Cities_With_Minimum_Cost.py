#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 16:43:58 2021

@author: jeff
"""

"""

Key Idea:
    Use Union Find
    Sort connections based on the cost
    Greedy
    Check if theres only one group

"""

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        parent = {i:i for i in range(1, n+1)}
        ans = 0
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            if find(x) == find(y):
                return False
            parent[find(y)] = find(x)
            return True
        
        connections.sort(key=lambda x: x[2])
        
        for x, y, cost in connections:
            if union(x, y):
                ans += cost
        return ans if len(set(find(x) for x in parent)) == 1 else -1