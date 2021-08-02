#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 12:30:18 2021

@author: jeff
"""

"""

Key Idea:
    Sort first and then iterate find max_h and max_w

"""

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        horizontalCuts.sort()
        verticalCuts.sort()
        max_h = 0
        max_v = 0
        horizontalCuts.append(h)
        verticalCuts.append(w)
        
        for index, cut in enumerate(horizontalCuts):
            if index == 0:
                max_h = cut
            elif horizontalCuts[index] - horizontalCuts[index-1] > max_h:
                max_h = horizontalCuts[index] - horizontalCuts[index-1]
        
        for index, cut in enumerate(verticalCuts):
            if index == 0:
                max_v = cut
            elif verticalCuts[index] - verticalCuts[index-1] > max_v:
                max_v = verticalCuts[index] - verticalCuts[index-1]
            
                    
        return max_h * max_v % 1_000_000_007