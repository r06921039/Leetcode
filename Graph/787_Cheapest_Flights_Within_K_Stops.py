#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 23:36:02 2021

@author: jeff
"""

"""
Key Idea:
    Using BFS and keep a distance dictionary with key (node, stops)
    Everytime pop a node and calculate its neighbor
"""

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        table = collections.defaultdict(list)
        distances = collections.defaultdict(lambda: float("inf"))
        distances[(src, 0)] = 0
        stops = 0
        ans = float("inf")
        
        for start, end, price in flights:
            table[start].append([end, price])
        
        queue = collections.deque([src])
        
        while queue and stops <= k:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                for neighbor, cost in table[node]:
                    if stops == k and neighbor != dst:
                        continue
                    du = distances[(node, stops)]
                    dv = distances[(neighbor, stops+1)]
                    if dv > du + cost:
                        distances[(neighbor, stops+1)] = du + cost
                        if neighbor == dst:
                            ans = min(ans, du+cost)
                        queue.append(neighbor)
            stops += 1
            
        return ans if ans != float("inf") else -1