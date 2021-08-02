#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 20:48:35 2021

@author: jeff
"""

"""

Key Idea:
    Use DFS

"""


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set()
        
        def dfs(index):
            if index in visited:
                return
            visited.add(index)
            for room in rooms[index]:
                dfs(room)
        dfs(0)

        for room in range(len(rooms)):
            if room not in visited:
                return False
            
        return True