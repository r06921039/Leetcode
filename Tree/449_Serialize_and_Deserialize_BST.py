#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 00:11:09 2021

@author: jeff
"""

"""
Key Idea:
    Use preorder to serialize
    And use min_val and max_val to decide left node or right node
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        ans = []
        def preorder(node):
            if node:
                ans.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return " ".join(ans)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        vals = collections.deque([int(val) for val in data.split(" ")])
        def helper(min_val, max_val):
            if vals and min_val < vals[0] < max_val:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = helper(min_val, val)
                node.right = helper(val, max_val)
                return node
        
        return helper(float("-inf"), float("inf"))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
        