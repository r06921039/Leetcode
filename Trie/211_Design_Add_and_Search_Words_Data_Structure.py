#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:42:45 2021

@author: jeff
"""

"""
Key Idea:
    Using Trie
"""

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
            
        node["$"] = True

    def search(self, word: str) -> bool:
        def searchInNode(word, node):
            for i, char in enumerate(word):
                if char not in node:
                    if char == ".":
                        for c in node:
                            if c != "$" and searchInNode(word[i+1:], node[c]):
                                return True
                    return False
                else:
                    node = node[char]
            return "$" in node
        
        return searchInNode(word, self.trie)