#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 15:07:44 2021

@author: jeff
"""

"""
Key Idea:
    Use DFS and keep top1 and top2 distance
    compare the max_diameter and top1+top2
"""
class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.diameter = 0
        def dfs(node):
            top1_distance, top2_distance = 0, 0
            if len(node.children) == 0:
                return 0
            for child in node.children:
                height = dfs(child) + 1
                if height > top1_distance:
                    top1_distance, top2_distance = height, top1_distance
                elif height > top2_distance:
                    top2_distance = height
            self.diameter = max(self.diameter, top1_distance + top2_distance)
            return top1_distance
        
        dfs(root)
        return self.diameter