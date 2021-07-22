#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 15:33:59 2021

@author: jeff
"""

"""

Key Idea:
    return sum and node numbers

"""
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        
        if not root:
            return 0
        
        self.ans = 0
        
        def recurse(node):
            if not node:
                return 0, 0
            right_sum, right_node_num = recurse(node.right)
            left_sum, left_node_num = recurse(node.left)
            cur_node_num = 1 + right_node_num + left_node_num
            cur_sum = node.val + right_sum + left_sum
            cur_avg = cur_sum / cur_node_num
            self.ans = max(self.ans, cur_avg)
            return cur_sum, cur_node_num
        
        recurse(root)
        
        return self.ans
            