#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 23:42:25 2021

@author: jeff
"""
"""

Key Idea:
    Dict with heap

"""


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        table = collections.defaultdict(list)

        for ID, score in items:
            heapq.heappush(table[ID], score)
            if len(table[ID]) > 5:
                heapq.heappop(table[ID])
        ans = []
        for key, value in table.items():
            ans.append([key, sum(value)//5])
        
        ans.sort()
        
        return ans
    
    
    
"""
Javascript
"""
var highFive = function(items) {
    var dict = {};
    for (item of items){
        var key = item[0];
        var value = item[1];
        if (key in dict){
            dict[key].enqueue(value);
            if (dict[key].size() > 5){
                dict[key].dequeue(); 
            }
        }
        else{
            dict[key] = new MinPriorityQueue();
            dict[key].enqueue(value);
        }
    }
    let ans = [];
    for (key in dict){
        var arr = dict[key].toArray();
        var sum = arr.reduce((total, value) => total + Number(value["element"]), 0);
        ans.push([Number(key), Math.floor(sum/5)]);
    }
    ans.sort((a,b) => a[0]-b[0]);
    return ans;
};