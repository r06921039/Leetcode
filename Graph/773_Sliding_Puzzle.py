#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 20:32:23 2021

@author: jeff
"""

"""
Key Idea:
    Use BFS to find minimum steps
"""
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        end = [[1, 2, 3], [4, 5, 0]]
        nrow, ncol = len(board), len(board[0])
        visited = []
        queue = collections.deque([board])
        steps = 0
        
        def findZero(matrix):
            for i in range(nrow):
                for j in range(ncol):
                    if matrix[i][j] == 0:
                        return i, j
        
        while queue:
            size = len(queue)
            for _ in range(size):
                matrix = queue.popleft()
                visited.append(copy.deepcopy(matrix))
                if matrix == end:
                    return steps
                i, j = findZero(matrix)
                for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                    if 0 <= i+di < nrow and 0 <= j+dj < ncol:
                        matrix[i][j], matrix[i+di][j+dj] = matrix[i+di][j+dj], matrix[i][j]
                        if matrix not in visited:
                            queue.append(copy.deepcopy(matrix))
                        matrix[i][j], matrix[i+di][j+dj] = matrix[i+di][j+dj], matrix[i][j]
            steps += 1
                
                    
        return -1
                