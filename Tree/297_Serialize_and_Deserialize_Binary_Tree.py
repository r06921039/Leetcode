#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 23:17:32 2021

@author: jeff
"""

"""
Key Idea:
    Use DFS(preorder) or BFS
"""

#DFS

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.string = ""
        def helper(node):
            if not node:
                self.string += "None,"
                return
            self.string += str(node.val) + ","
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return self.string
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.vals = data.split(",")
        
        def helper():
            if self.vals[0] == "None":
                self.vals.pop(0)
                return None
            node = TreeNode(int(self.vals[0]))
            self.vals.pop(0)
            node.left = helper()
            node.right = helper()
            return node
        
        return helper()
    
#BFS

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = collections.deque([root])
        self.string = ""
        while queue:
            node = queue.popleft()
            if not node:
                self.string += "None,"
            else:
                self.string += str(node.val) + ","
                queue.append(node.left)
                queue.append(node.right)
        return self.string

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.vals = data.split(",")
        root = TreeNode(int(self.vals[0])) if self.vals[0] != "None" else None
        if not root:
            return None
        queue = collections.deque([root])
        self.vals.pop(0)
        while queue:
            node = queue.popleft()
            node.left = TreeNode(int(self.vals[0])) if self.vals[0] != "None" else None
            self.vals.pop(0)
            node.right = TreeNode(int(self.vals[0])) if self.vals[0] != "None" else None
            self.vals.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root