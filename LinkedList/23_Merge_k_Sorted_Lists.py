#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 20:33:46 2021

@author: jeff
"""

"""
Key Idea:
    Use minheap to store first node of every list, and pop it every time
    Or use merge every two list 
"""

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode(-1)
        tail = dummy
        for l_id, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, l_id, l))
        
        while heap:
            val, l_id, node = heapq.heappop(heap)
            tail.next = node
            if node.next:
                node = node.next
                heapq.heappush(heap, (node.val, l_id, node))
            tail = tail.next
            
        return dummy.next
    
    

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergeTwoLists(l1, l2):
            dummy = ListNode(-1)
            tail = dummy
            while l1 and l2:
                if l1.val > l2.val:
                    tail.next = l2
                    l2 = l2.next
                    tail = tail.next
                else:
                    tail.next = l1
                    l1 = l1.next
                    tail = tail.next
            
            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            
            return dummy.next
        
        def mergeLists(lists, l, r):
            if l > r:
                return None
            elif l == r:
                return lists[l]
            elif l == r - 1:
                return mergeTwoLists(lists[l], lists[r])
            else:
                mid = (l + r) // 2
                l1 = mergeLists(lists, l, mid)
                l2 = mergeLists(lists, mid+1, r)
                return mergeTwoLists(l1, l2)
            
        return mergeLists(lists, 0, len(lists) - 1)