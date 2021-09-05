#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 22:47:51 2021

@author: jeff
"""

"""
Key Idea:
    Store prefix product
    if num == 0 then set stack to [1]
    else append stack[-1] * num
    len() is constant
"""
class ProductOfNumbers:

    def __init__(self):
        self.stack = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.stack = [1]
        else:
            self.stack.append(self.stack[-1] * num)
        

    def getProduct(self, k: int) -> int:
        if k >= len(self.stack):
            return 0
        else:
            return self.stack[-1] // self.stack[-k-1]
        
