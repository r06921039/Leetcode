#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 00:15:27 2021

@author: jeff
"""

"""
Key Idea:
    Use "#" to indicate no more children, continue serialization from parent
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        serial = []
        def preorder(node):
            if not node:
                return 
            serial.append(str(node.val))
            for child in node.children:
                preorder(child)
            serial.append("#")
            
        preorder(root)
        return ",".join(serial)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        
        self.vals = data.split(",")
        root = Node(int(self.vals.pop(0)), [])
        
        def helper(node):
            
            while self.vals and self.vals[0] != "#":
                child = Node(int(self.vals.pop(0)), [])
                node.children.append(child)
                helper(child)
                
            self.vals.pop(0) # pop "#"
        
        helper(root)
        return root