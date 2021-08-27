#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 17:17:58 2021

@author: jeff
"""

"""
Key Idea:
    Think of Bipartite graph, we need to create a graph and neighbor node should be drawed in different color.
"""

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if n == 1 or not dislikes:
            return True
        
        NOT_COLORED, BLUE, GREEN = 0, 1, -1
        graph = collections.defaultdict(list)
        color_table = [NOT_COLORED] * (n+1)
        
        for i, j in dislikes:
            graph[i].append(j)
            graph[j].append(i)
        
        def dfs(node, color):
            
            color_table[node] = color
            
            for neighbor in graph[node]:
                if color_table[neighbor] == color:
                    return False
                if color_table[neighbor] == NOT_COLORED and not dfs(neighbor, -color):
                    return False
            
            return True
        
        for node in range(1, n+1):
            if color_table[node] == NOT_COLORED and not dfs(node, BLUE):
                return False
        return True