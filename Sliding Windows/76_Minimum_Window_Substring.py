#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 22:34:05 2021

@author: jeff
"""

"""
Key Idea:
    Sliding window and use another dict to count the word
    compare formed and required
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = collections.Counter(t)
        window_count = collections.defaultdict(int)
        formed = 0
        required = len(counter)
        start = 0
        min_length = float("inf")
        ans = ""
        for i, char in enumerate(s):
            if char in counter:
                window_count[char] += 1
                if window_count[char] == counter[char]:
                    formed += 1
            while formed == required:
                if i - start + 1 < min_length:
                    min_length = i - start + 1
                    ans = s[start: start + min_length]
                if s[start] in counter:
                    window_count[s[start]] -= 1
                    if window_count[s[start]] < counter[s[start]]:
                        formed -= 1
                start += 1
            
        
        return ans