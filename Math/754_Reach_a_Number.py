#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 17:16:26 2021

@author: jeff
"""

"""
Key Idea:
    Add 1 to n first which is bigger than target, then start to check if n(n+1)/2 - t is even
    If not then n += 1
"""

class Solution:
    def reachNumber(self, target: int) -> int:
        t = abs(target)
        n = math.floor(math.sqrt(2*t))
        while True:
            minus = n*(n+1)/2 - t
            if minus >= 0 and minus % 2 == 0 :
                return n
            n += 1