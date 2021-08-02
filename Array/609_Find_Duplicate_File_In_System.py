#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 17:59:28 2021

@author: jeff
"""

"""

Key Idea:
    Use hash, content as key

Follow up:
    Imagine you are given a real file system, how will you search files? DFS or BFS?
    core idea: DFS
    Reason: if depth of directory is not too deeper, which is suitable to use DFS, comparing with BFS.


    If the file content is very large (GB level), how will you modify your solution?
    core idea: make use of meta data, like file size before really reading large content.
    Two steps:
    DFS to map each size to a set of paths that have that size: Map<Integer, Set>
    For each size, if there are more than 2 files there, compute hashCode of every file by MD5, if any files with the same size have the same hash, then they are identical files: Map<String, Set>, mapping each hash to the Set of filepaths+filenames. This hash id's are very very big, so we use the Java library BigInteger.
    To optimize Step-2. In GFS, it stores large file in multiple "chunks" (one chunk is 64KB). we have meta data, including the file size, file name and index of different chunks along with each chunk's checkSum(the xor for the content). For step-2, we just compare each file's checkSum.
    Disadvantage: there might be flase positive duplicates, because two different files might share the same checkSum.
    
    If you can only read the file by 1kb each time, how will you modify your solution?
    makeHashQuick Function is quick but memory hungry, might likely to run with java -Xmx2G or the likely to increase heap space if RAM avaliable.
    we might need to play with the size defined by "buffSize" to make memory efficient.
    
    
    What is the time complexity of your modified solution? What is the most time-consuming part and memory-consuming part of it? How to optimize?
    Answer:
    hashing part is the most time-consuming and memory consuming.
    optimize as above mentioned, but also introduce false positive issue.

    
    How to make sure the duplicated files you find are not false positive?
    Answer:
    Question-2-Answer-1 will avoid it.
    We need to compare the content chunk by chunk when we find two "duplicates" using checkSum.

"""

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        memo = {}
        
        for path in paths:
            path = path.split(" ")
            file_path = path[0]
            for file_name in path[1:]:
                file_name = file_name.split("(")
                if file_name[1] not in memo:
                    memo[file_name[1]] = [file_path + "/" + file_name[0]]
                else:
                    memo[file_name[1]].append(file_path + "/" + file_name[0])
                    
        return [values for key, values in memo.items() if len(values) > 1]