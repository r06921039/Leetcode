#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 20:41:44 2021

@author: jeff
"""

"""
Key Idea:
    Prevent using the same number by iterating through counter
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = collections.Counter(nums)
        ans = []
        def dfs(prefix, length):
            if length == len(nums):
                ans.append(list(prefix))
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    prefix.append(num)
                    dfs(prefix, length + 1)
                    prefix.pop()
                    counter[num] += 1
        dfs([], 0)
        return ans