#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 16:54:44 2021

@author: jeff
"""

"""

Key Idea:
    Sort first with Counter (ball_number, count)
    Calculate sell, whole, remainder with divmod
    Add cost
    Orders substract sell
    Add index
"""



class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        array = sorted(Counter(inventory).items(), reverse=True) + [(0, 0)]
        ans = 0
        index = 0
        width = 0
        while orders > 0:
            width += array[index][1]
            sell = min(orders, width * (array[index][0] - array[index+1][0]))
            whole, remainder = divmod(sell, width)
            ans += (width * (array[index][0] + array[index][0] - whole + 1)*whole // 2) + remainder*(array[index][0] - whole)
            orders -= sell
            index += 1
        return ans % int(1E9 + 7)