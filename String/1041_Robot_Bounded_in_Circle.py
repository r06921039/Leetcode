#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 22:44:29 2021

@author: jeff
"""

"""

Key Idea:
    Check if the robot is in the same position or it change direction

"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        angle = 90
        position = [0, 0]
        for instruction in instructions:
            if instruction == "L":
                angle += 90
            elif instruction == "R":
                angle -= 90
            else:
                while angle < 0:
                    angle += 360
                direction = angle % 360
                if direction == 90:
                    position[1] += 1
                elif direction == 180:
                    position[0] -= 1
                elif direction == 270:
                    position[1] -= 1
                else:
                    position[0] += 1
        
        return True if position == [0, 0] or angle % 360 != 90 else False