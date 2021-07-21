#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 16:35:18 2021

@author: jeff
"""

"""

Key idea:
    Iterate over the array. At each step :

        Clean the deque :

            Keep only the indexes of elements from the current sliding window.

            Remove indexes of all elements smaller than the current one, since they will not be the maximum ones.

        Append the current element to the deque.

        Append deque[0] to the output.

"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = collections.deque()
        out = []
        for i, num in enumerate(nums):
            if d:
                if d[0] <= i - k:
                    d.popleft()
                while d and nums[d[-1]] < num:
                    d.pop()
            d.append(i)
            if i >= k-1:
                out.append(nums[d[0]])
        return out