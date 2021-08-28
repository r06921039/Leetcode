#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 23:12:51 2021

@author: jeff
"""

"""
Key Idea:
    Sort with the end day, and keep a heap of the duration, while the total exceed the end day
    pop out the longest duration.
"""

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: x[1])
        heap = []
        total = 0
        
        for duration, last_day in courses:
            total += duration
            heapq.heappush(heap, -duration)
            while total > last_day:
                total += heapq.heappop(heap)
        return len(heap)