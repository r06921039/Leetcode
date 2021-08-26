#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 23:26:09 2021

@author: jeff
"""

"""
Key Idea:
    keep l and r, use count to find r and then prev = r, cur = l
    and then update jump: 
        jump.next, jump, l = prev, l, r
"""
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
        while True:
            count = 0
            while r and count < k:
                r = r.next
                count += 1
            if count == k:
                prev, cur = r, l
                for _ in range(k):
                    cur.next, cur, prev = prev, cur.next, cur
                jump.next, jump, l = prev, l, r
            else:
                return dummy.next