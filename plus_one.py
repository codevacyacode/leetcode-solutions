# -*- coding: utf-8 -*-
"""
Created on Thu May 19 16:24:46 2022

@author: codevacyacode

https://leetcode.com/problems/plus-one/

Runtime: 42 ms, faster than 57.58% of Python3 online submissions for Plus One.
Memory Usage: 13.9 MB, less than 59.47% of Python3 online submissions 
for Plus One.
"""

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        addition = True
        i = len(digits) - 1
        while addition:
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                    addition = False
                else:
                    i -= 1
            else:
                digits[i] += 1
                addition = False
            
        return digits