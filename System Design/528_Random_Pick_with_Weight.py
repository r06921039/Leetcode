#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 22:17:41 2021

@author: jeff
"""

"""
Key Idea:
    Keep a running sum and Use binary search
"""

class Solution:

    def __init__(self, w: List[int]):
        self.running_sum = []
        total = 0
        for weight in w:
            total += weight
            self.running_sum.append(total)
            
    def pickIndex(self) -> int:
        low = 0
        high = len(self.running_sum)
        target = random.randint(1, self.running_sum[-1])
        while low < high:
            mid = (low + high) // 2
            if self.running_sum[mid] == target:
                return mid
            elif self.running_sum[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low