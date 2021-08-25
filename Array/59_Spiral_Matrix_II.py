#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 15:46:19 2021

@author: jeff
"""

"""
Key Idea:
    Create a A = [[n*n]] and add the list on the top everytime and spin
"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A = [[n*n]]
        while A[0][0] > 1:
            A = [range(A[0][0] - len(A), A[0][0])] + list(zip(*A[::-1]))
        A = list(map(list, A))
        return A




class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A = [[0 for _ in range(n)] for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(1, n*n+1):
            A[i][j] = k
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A