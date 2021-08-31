#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:55:50 2021

@author: jeff
"""

"""
Key Idea:
    Use DFS to run all the gates, or use BFS to put all gates in the queue
"""

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        nrow = len(rooms)
        ncol = len(rooms[0])
        
        
        def dfs(i, j, length):
            if length >= rooms[i][j]:
                return 
            if rooms[i][j] != 0:
                rooms[i][j] = length
            if length == float("-inf"):
                length = 0
            
            for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                if 0 <= di+i < nrow and 0 <= dj+j < ncol and rooms[di+i][dj+j] != -1:
                    dfs(di+i, dj+j, length + 1)
            
        for i in range(nrow):
            for j in range(ncol):
                if rooms[i][j] == 0:
                    dfs(i, j, float("-inf"))