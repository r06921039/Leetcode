#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 17:02:20 2021

@author: jeff
"""

""" 

Key Idea:
    Use the same idea as Best Time to Buy and Sell Stock III
    but instead using a length k array to store and iterate
    
"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0
        n = len(prices)
        ans = 0
        if k >= n/2:
            for i in range(1, n):     
                if prices[i] - prices[i-1] > 0:
                    ans += prices[i] - prices[i-1]
            return ans
        
        buy_k = [float("-inf")] * (k)
        buy_k[0] = float("inf")
        profit_k = [0] * (k)
        
        for price in prices:
            for i in range(k):
                buy_k[i] = min(buy_k[i], price) if i == 0 else max(buy_k[i], profit_k[i-1] - price)
                profit_k[i] = max(profit_k[i], price - buy_k[i]) if i == 0 else max(profit_k[i], buy_k[i] + price)
                
        return profit_k[k-1]
                