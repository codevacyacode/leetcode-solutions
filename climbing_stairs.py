# -*- coding: utf-8 -*-
"""
Created on Tue May 17 15:58:31 2022

@author: codevacyacode

https://leetcode.com/problems/climbing-stairs/

Runtime: 30 ms, faster than 87.65% of Python3 online submissions 
for Climbing Stairs.
Memory Usage: 13.9 MB, less than 58.36% of Python3 online submissions 
for Climbing Stairs.
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [1, 2, 3]
        if n < 4:
            return n 
        else:
            while n > 3:
                ways[0] = ways[1]
                ways[1] = ways[2]
                ways[2] = ways[0] + ways[1]
                n -= 1
            return ways[2]