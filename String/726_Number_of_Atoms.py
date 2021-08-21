#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 17:03:33 2021

@author: jeff
"""

"""
Key Idea:
    Iterate the string from right to left
    and solve it like decode string
"""
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        count = 0
        element = ""
        coeff = 1
        stack = []
        i = 0
        table = collections.defaultdict(int)
        ans = ""
        for char in formula[::-1]:
            if char.isdigit():
                count += int(char) * (10**i)
                i += 1
            elif char == ")":
                coeff *= count if count != 0 else 1
                stack.append(count if count != 0 else 1)
                count = 0
                i = 0
            elif char == "(":
                coeff //= stack.pop() if stack else 1
            elif char.isupper():
                element = char + element
                table[element] += coeff * (count if count != 0 else 1)
                count = 0
                i = 0
                element = ""
            elif char.islower():
                element += char
        
        for key in sorted(table.keys()):
            ans += key + (str(table[key]) if table[key] != 1 else "")
        
        return ans