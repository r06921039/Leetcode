#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 17:54:22 2021

@author: jeff
"""

"""
Key Idea:
    Using 2069(prime number) as key number
    and for every key store a Bucket which implemented by array
"""

class Bucket:
    def __init__(self):
        self.bucket = []

    def update(self, key, value):
        found = False
        for i, element in enumerate(self.bucket):
            if element[0] == key:
                self.bucket[i] = (key, value)
                found = True
                return
        if not found:
            self.bucket.append((key, value))
    
    def get(self, key):
        for k, v in self.bucket:
            if k == key:
                return v
        return -1
    
    def remove(self, key):
        for i, element in enumerate(self.bucket):
            if element[0] == key:
                del self.bucket[i]
                

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_number = 2069
        self.hash_map = [Bucket() for _ in range(self.key_number)]
        
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_key = key % self.key_number
        self.hash_map[hash_key].update(key, value)
        
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = key % self.key_number
        return self.hash_map[hash_key].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = key % self.key_number
        self.hash_map[hash_key].remove(key)