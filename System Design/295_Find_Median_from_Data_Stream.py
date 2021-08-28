#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 21:45:39 2021

@author: jeff
"""

"""
Key Idea:
    Keep two heap, max_heap for first half of array and min_heap for second half of array.
    Keep len(max_heap) == len(min_heap) or len(max_heap) == len(min_heap) + 1
"""

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == len(self.max_heap):
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        else:
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + -self.max_heap[0]) / 2
        else:
            return self.min_heap[0]
