#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 19:13:08 2021

@author: jeff
"""

"""

Key Idea:
    getMask:
    0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 1 0 0 0 1
    z y x w v u t s r q p o n m l k j i h g f e d c b a
    
    Create mask_freq: count the number of same mask for word
    
    Generate every possible submask for puzzle by doing (subMask - 1) & originalMask
    add count to the ans
    Break while submask equal to zero
    
    return ans

"""

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        
        def getMask(word):
            mask = 0
            for letter in word:
                offset = ord(letter) - ord("a")
                mask |= 1 << offset
            return mask
        
        mask_freq = {}
        
        for word in words:
            mask = getMask(word)
            if mask in mask_freq:
                mask_freq[mask] += 1
            else:
                mask_freq[mask] = 1
                
        ans = [0] * len(puzzles)
        
        for i, puzzle in enumerate(puzzles):
            puzzle_mask = getMask(puzzle)
            submask = puzzle_mask
            first_word_index = ord(puzzle[0]) - ord("a")
            while True:
                if submask >> first_word_index & 1:
                    ans[i] += mask_freq.get(submask, 0)
                if submask == 0:
                    break
                submask = (submask - 1) & puzzle_mask
        
        return ans