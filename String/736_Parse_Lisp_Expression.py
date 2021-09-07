#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 23:13:31 2021

@author: jeff
"""

"""
Key Idea:
    Use stack to store tokens and table, remember to evaluate everytime when tokens[0] is let
    Remember to use dict(table) to copy a new dictionary
"""

class Solution:
    def evaluate(self, expression: str) -> int:
        tokens, stack, table = [""], [], {}
        
        def evaluate(token):
            if token[0] in ["add", "mult"]:
                n1, n2 = int(table.get(token[1], token[1])), int(table.get(token[2], token[2]))
                return str(n1+n2) if token[0] == "add" else str(n1*n2)
            else:
                for i in range(1, len(token)-2, 2):
                    table[token[i]] = table.get(token[i+1], token[i+1])
                return table.get(token[-1], token[-1])
        
        for char in expression:
            print(tokens, table)
            if char == "(":
                if tokens[0] == "let":
                    evaluate(tokens)
                stack.append([tokens, dict(table)])
                tokens = [""]
            elif char == ")":
                val = evaluate(tokens)
                tokens, table = stack.pop()
                tokens[-1] += val
            elif char == " ":
                tokens.append("")
            else:
                tokens[-1] += char
                
        return int(tokens[0])