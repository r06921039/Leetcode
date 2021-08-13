#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 23:18:57 2021

@author: jeff
"""

"""
Key Idea:
    Two pointer
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if not chars:
            return 0
        if n == 1:
            return 1
        
        chars.append("end")
        new_ptr = 0
        count = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                chars[new_ptr] = chars[i-1]
                new_ptr += 1
                if count != 1:
                    repeat = list(str(count))
                    n_repeat = len(repeat)
                    chars[new_ptr: new_ptr + n_repeat] = repeat
                    new_ptr += n_repeat
                    count = 1
                    
        while n != new_ptr-1:
            chars.pop()
            n -= 1
        
        return len(chars)