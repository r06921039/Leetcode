#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 22:55:43 2021

@author: jeff
"""

"""
Key Idea:
    Keep a heap with (nums1[idx1]+nums2[idx2], idx1, idx2)
    Pop it and push (nums1[idx1+1]+nums2[idx2], idx1+1, idx2), (nums1[idx1]+nums2[idx2+1], idx1, idx2+1)
"""

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1 = len(nums1)
        n2 = len(nums2)
        heap = [(nums1[0]+nums2[0], 0, 0)]
        visited = set()
        visited.add((0,0))
        count = 0
        ans = []
        
        while count < k and heap:
            val, idx1, idx2 = heapq.heappop(heap)
            ans.append([nums1[idx1], nums2[idx2]])
            if idx1 + 1 < n1 and (idx1+1, idx2) not in visited:
                heapq.heappush(heap, (nums1[idx1+1]+nums2[idx2], idx1+1, idx2))
                visited.add((idx1+1, idx2))
            if idx2 + 1 < n2 and (idx1, idx2+1) not in visited:
                heapq.heappush(heap, (nums1[idx1]+nums2[idx2+1], idx1, idx2+1))
                visited.add((idx1, idx2+1))
            count += 1
        
        return ans