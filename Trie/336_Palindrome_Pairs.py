#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 21:31:29 2021

@author: jeff
"""

"""
Key Idea:
    Remember 3 cases:
        1. Reversed word and word is palindrome
        2. Prefix is palindrome
        3. Suffix is palindrome
"""

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        def allValidPrefixes(word):
            valid_prefixes = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    valid_prefixes.append(word[:i])
            return valid_prefixes
        
        def allValidSuffixes(word):
            valid_suffixes = []
            for i in range(len(word)):
                if word[:i+1] == word[:i+1][::-1]:
                    valid_suffixes.append(word[i+1:])
            return valid_suffixes
        
        
        word_index = {word: i for i, word in enumerate(words)}
        solutions = []
        
        for idx, word in enumerate(words):
            
            if word[::-1] in word_index and idx != word_index[word[::-1]]:
                solutions.append([idx, word_index[word[::-1]]])
                
            for suffix in allValidSuffixes(word):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_index:
                    solutions.append([word_index[reversed_suffix], idx])
                    
            for prefix in allValidPrefixes(word):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_index:
                    solutions.append([idx, word_index[reversed_prefix]])
                    
        return solutions