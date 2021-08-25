#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 23:58:05 2021

@author: jeff
"""

"""
Key Idea:
    Keep 3 flags: seen_digit = seen_exponent = seen_dot = False
    Only 4 cases:
        1. isdigit
        2. in ["+", "-"]
        3. in ["e", "E"]
        4. == "."
        5. else return False
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = seen_exponent = seen_dot = False
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in ["+", "-"]:
                if i > 0 and s[i-1] not in ["e", "E"]:
                    return False
            elif char in ["e", "E"]:
                if not seen_digit or seen_exponent:
                    return False
                seen_exponent = True
                seen_digit = False
            elif char == ".":
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False
            
        return seen_digit