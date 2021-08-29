#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 22:07:10 2021

@author: jeff
"""

"""
Key Idea:
    Dfs all possible solution
"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        if len(s) > 12:
            return []
        
        ans = []
        path = []
        
        def dfs(count, string):
            if count > 4:
                return
            if not string and count != 4:
                return
            if not string and count == 4:
                str_path = ".".join(list(map(str, path)))
                ans.append(str_path)
                return
            for i in range(1, 4):
                if i > 1 and string[0] == "0":
                    continue
                if i <= len(string) and int(string[:i]) <= 255:
                    path.append(int(string[:i]))
                    dfs(count+1, string[i:])
                    path.pop()
        dfs(0, s)
        
        return ans