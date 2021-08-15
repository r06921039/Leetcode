#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 01:30:30 2021

@author: jeff
"""

"""
Key Idea:
    remember minCoin(total) and everytime check minCoin(total - coin)
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count = {}
        
        def minCoin(total):
            if total < 0:
                return -1
            if total == 0:
                return 0
            if total in count:
                return count[total]
            min_count = float("inf")
            for coin in coins:
                res = minCoin(total - coin)
                if res >= 0 and res < min_count:
                    min_count = 1 + res
            count[total] = min_count if min_count != float("inf") else -1
            return count[total]
        
        return minCoin(amount)
    
    
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        
        return dp[amount] if dp[amount] != float("inf") else -1