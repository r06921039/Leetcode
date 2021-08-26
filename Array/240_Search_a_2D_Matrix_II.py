#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 11:21:25 2021

@author: jeff
"""

"""
Key Idea:
    Start from bottom left and if element < target, col += 1 else row -= 1
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrow = len(matrix)
        if nrow == 0:
            return False
        ncol = len(matrix[0])
        
        i, j = nrow-1, 0
        
        while i >= 0 and j < ncol:
            element = matrix[i][j]
            if element == target:
                return True
            elif element < target:
                j += 1
            else:
                i -= 1
                
        return False