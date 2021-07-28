#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 15:42:07 2021

@author: jeff
"""
"""

Key Idea:
    check requestTime[i] - requestTime[i-n]

"""

def droppedRequest(requestTime, n):
    ans = 0 
    for i in range(n):
        if i > 2 and requestTime[i] == requestTime[i-3]:
                ans += 1
        elif i > 19 and (requestTime[i] - requestTime[i-20]) < 10:
            ans += 1
        elif i > 59 and requestTime[i] - requestTime[i-60] < 60:
            ans += 1
            
        