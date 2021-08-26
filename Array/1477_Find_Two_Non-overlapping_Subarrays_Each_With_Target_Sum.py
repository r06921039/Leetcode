#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 22:50:39 2021

@author: jeff
"""

"""
Key Idea:
    Keep a array best_till to record the shortest array before index i
    when find a new array, compare ans and i - end + best_till[end]
"""

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        best_till = [float("inf")] * n
        table = {0: -1}
        running_sum = 0
        best = ans = float("inf")
        for i, num in enumerate(arr):
            running_sum += num
            if running_sum - target in table:
                end = table[running_sum - target]
                if end != -1:
                    ans = min(ans, i - end + best_till[end])
                best = min(best, i-end)
            best_till[i] = best
            table[running_sum] = i
        
        return ans if ans != float("inf") else -1