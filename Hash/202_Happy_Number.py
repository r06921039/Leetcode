#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 22:31:07 2021

@author: jeff
"""

"""
Key Idea:
    Keep Hashmap and detect cycle
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        def getNext(n):
            total = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total += digit ** 2
            return total
        
        while True:
            if n in visited:
                return False
            if n == 1:
                return True
            visited.add(n)
            n = getNext(n)