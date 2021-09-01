#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 21:27:00 2021

@author: jeff
"""

"""
Key Idea:
    Use Trie and keep count in each node
    Find the index with count == 1
    Abbrev the word
"""

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.count = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            node.count += 1
            node = node.children[char]
            
    def find(self, word):
        node = self.root
        for i, char in enumerate(word):
            if node.count == 1:
                return i
            node = node.children[char]


class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        def abbrev(word, i=1):
            if len(word) - i < 3:
                return word
            return word[:i] + str(len(word)-1-i) + word[-1]
        
        group = collections.defaultdict(list)
        ans = {}
        
        for word in words:
            group[abbrev(word)].append(word)
            
        for abbr, group_words in group.items():
            if len(group_words) > 1:
                trie = Trie()
                for word in group_words:
                    trie.insert(word)
                
                for word in group_words:
                    index = trie.find(word)
                    ans[word] = abbrev(word, index)
                
            else:
                ans[group_words[0]] = abbr
                
                
        return [ans[word] for word in words]