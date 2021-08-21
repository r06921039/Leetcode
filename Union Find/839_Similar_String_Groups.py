#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 17:34:12 2021

@author: jeff
"""

"""
Key Idea:
    Compare every string which is O(n^2)
    Use sum(a[i][k] != a[j][k] for k in range(len(a[i]))) in (0, 2) as condition
"""


class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        self.parents[root_y] = root_x
            
    def count(self):
        for i in range(len(self.parents)):
            self.find(i)
        return len(set(self.parents))


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        n = len(strs)
        union_set = UnionFind(n)
        for i in range(n):
            for j in range(1, n):
                if sum(strs[i][k] != strs[j][k] for k in range(len(strs[i]))) in (0, 2):
                    union_set.union(i, j)
        
        return union_set.count()