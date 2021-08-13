#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 21:55:47 2021

@author: jeff
"""

"""
Key Idea:
    Use dict to store (key, value) : (remainder, len(result))
"""

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        quotient, remainder = divmod(abs(numerator), abs(denominator))
        sign = "-" if numerator * denominator < 0 else ""
        if remainder == 0:
            return sign + str(quotient)
        result = [sign + str(quotient), "."]
        remainders = {}
        
        while remainder > 0 and remainder not in remainders:
            remainders[remainder] = len(result)
            quotient, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(quotient))
        
        if remainder in remainders:
            idx = remainders[remainder]
            result.insert(idx,"(")
            result.append(")")
        
        return "".join(result)