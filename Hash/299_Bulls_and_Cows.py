#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 16:30:57 2021

@author: jeff
"""

"""
Key Idea:
    Create a counter for secret first, and iterate guess
    Check if table_secret[char] <= 0, which B use before A
"""

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        table_secret = collections.Counter(secret)
        A = 0
        B = 0
        for i, char in enumerate(guess):
            if char in table_secret:
                if char == secret[i]:
                    A += 1
                    B -= int(table_secret[char] <= 0)
                else:
                    B += int(table_secret[char] > 0)
                table_secret[char] -= 1
                
        
                
        return str(A) + "A" + str(B) + "B"