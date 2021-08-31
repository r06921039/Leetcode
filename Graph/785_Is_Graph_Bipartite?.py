#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:13:13 2021

@author: jeff
"""

"""
Key Idea:
    Draw neighbor with different color, if neighbor has the same color with the current node
    return False
"""

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        NOT_COLORED, BLUE, GREEN = 0, 1, -1
        color_table = [0] * len(graph)
        
        def dfs(node, color):
            color_table[node] = color
            for neighbor in graph[node]:
                if color_table[neighbor] == color:
                    return False
                if color_table[neighbor] == NOT_COLORED and not dfs(neighbor, -color):
                    return False
            return True
        
        for i in range(len(graph)):
            if color_table[i] == NOT_COLORED and not dfs(i, BLUE):
                return False
            
        return True