#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 15:36:28 2021

@author: jeff
"""

"""
Key Idea:
    Keep monotonic stack, the answer will be the smallest possible int.
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if k == len(num):
            return "0"
        
        stack = collections.deque()
        count = 0
        for char in num:
            if not stack:
                stack.append(int(char))
            else:
                while count < k and stack and stack[-1] > int(char):
                    stack.pop()
                    count += 1
                stack.append(int(char))
        
        while count < k:
            stack.pop()
            count += 1

        return str(int("".join(list(map(str, stack)))))