#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 23:21:08 2021

@author: jeff
"""

"""
Key Idea:
    Use if to indicate duplicate and keep skipping, else prev = prev.next
"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode(float("inf"), head) 
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = prev.next
                
            curr = curr.next
        
        return dummy.next