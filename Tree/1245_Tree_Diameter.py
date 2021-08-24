#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 22:27:10 2021

@author: jeff
"""

"""
Key Idea:
    Use BFS first to find far_node and use far_node BFS again
    Use DFS to store top1_distance and top2_distance
    return top1_distance and top2_distance
"""

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        self.graph = collections.defaultdict(list)
        
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        def bfs(node):
            queue = collections.deque([node])
            visited = set()
            distance = -1
            far_node = None
            while queue:
                size = len(queue)
                for _ in range(size):
                    cur_node = queue.popleft()
                    visited.add(cur_node)
                    for neighbor in self.graph[cur_node]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            far_node = neighbor
                distance += 1
            
            return distance, far_node
        
        _, far_node = bfs(0)
        distance, _ = bfs(far_node)
        return distance