#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 21:59:59 2021

@author: jeff
"""

"""
Key Idea:
    Helper return min_val, max_val, is_bst, node_n
"""

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.res = 0
        
        def helper(node):
            if not node:
                return float("inf"), float("-inf"), True, 0
            
            left_min, left_max, is_left_bst, left_n = helper(node.left)
            right_min, right_max, is_right_bst, right_n = helper(node.right)
            if left_max < node.val < right_min and is_left_bst and is_right_bst:
                self.res = max(self.res, 1 + left_n + right_n)
            else:
                return 0, 0, False, 0
            
            return min(node.val, left_min), max(node.val, right_max), True, 1 + left_n + right_n
        
        helper(root)
        
        return self.res