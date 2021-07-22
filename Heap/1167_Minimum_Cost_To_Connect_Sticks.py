#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 21:59:52 2021

@author: jeff
"""

"""

Key Idea:
Always connect the shortest two stick.
Use Heap
Heappop two sticks and connect
Then Heappush back the new stick

"""

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        res = 0
        while len(sticks) > 1:
            x, y = heapq.heappop(sticks), heapq.heappop(sticks)
            res += x + y
            heapq.heappush(sticks, x + y)
        return res