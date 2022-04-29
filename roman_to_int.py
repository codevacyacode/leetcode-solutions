# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 10:36:11 2022

@author: codevacyacode
"""
# https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        
        for i in range(len(s)-1, -1, -1):
            if s[i] == 'I':
                if result < 5:
                    result += 1
                else:
                    result -= 1
            elif s[i] == 'V':
                result += 5
            elif s[i] == 'X':
                if result < 50:
                    result += 10
                else:
                    result -= 10 
            elif s[i] == 'L':
                result += 50
            elif s[i] == 'C':
                if result < 500:
                    result += 100
                else:
                    result -= 100
            elif s[i] == 'D':
                result += 500
            elif s[i] == 'M':
                result += 1000
        
        return result 