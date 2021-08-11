#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 23:42:25 2021

@author: jeff
"""
"""

Key Idea:
    Dict with heap

"""


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        table = collections.defaultdict(list)

        for ID, score in items:
            heapq.heappush(table[ID], score)
            if len(table[ID]) > 5:
                heapq.heappop(table[ID])
        ans = []
        for key, value in table.items():
            ans.append([key, sum(value)//5])
        
        ans.sort()
        
        return ans