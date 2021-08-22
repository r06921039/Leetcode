#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 23:18:47 2021

@author: jeff
"""

"""
Key Idea:
    Use recursive or iterative with stack
"""

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ret = 0
        stack = [(root, 1)]
        while stack:
            node, cnt = stack.pop()
            if node.left:
                stack.append((node.left, cnt+1 if node.left.val == node.val + 1 else 1))
            if node.right:
                stack.append((node.right, cnt+1 if node.right.val == node.val + 1 else 1))
            ret = max(ret, cnt)

        return ret
    
    
    
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.ans = 1
        
        def recurse(node):
            if not node:
                return None, 0
            right_val, right_len = recurse(node.right)
            left_val, left_len = recurse(node.left)
            if right_val is not None and right_val - 1 == node.val and right_len >= left_len:
                self.ans = max(self.ans, right_len+1)
                return node.val, right_len + 1
            elif left_val is not None and left_val - 1 == node.val and left_len >= right_len:
                self.ans = max(self.ans, left_len+1)
                return node.val, left_len + 1
            else:
                return node.val, 1
            
        recurse(root)
        
        return self.ans