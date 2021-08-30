#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 23:25:33 2021

@author: jeff
"""

"""
Key Idea:
    First k -= 1 cause its 0-index, and divid k by (n-1)! everytime
    index, k = divmod(k, (n-1)!)
"""

import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [i for i in range(1, n+1)]
        k -= 1
        ans = ""
        
        while n > 0:
            n -= 1
            idx, k = divmod(k, math.factorial(n))
            ans += str(numbers[idx])
            numbers.remove(numbers[idx])
        
        return ans