#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 11:12:35 2021

@author: jeff
"""

"""
Key Idea:
    change index to 2d index: mid = matrix[mid//ncol][mid%ncol]
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrow = len(matrix)
        if nrow == 0:
            return False
        ncol = len(matrix[0])
        
        low, high = 0, nrow * ncol
        
        while low < high:
            mid = (low + high) // 2
            element = matrix[mid//ncol][mid%ncol]
            if element == target:
                return True
            elif element < target:
                low = mid + 1
            else:
                high = mid
                
        return False