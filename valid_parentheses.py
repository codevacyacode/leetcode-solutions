# -*- coding: utf-8 -*-
"""
Created on Sun May 01 13:31:18 2022

@author: codevacyacode
"""
""" 
	https://leetcode.com/problems/valid-parentheses/
	Runtime: 27 ms, 
    faster than 95.80% of Python3 online submissions for Valid Parentheses.
	Memory Usage: 13.9 MB, 
    less than 72.61% of Python3 online submissions for Valid Parentheses.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        answer = True
        waiting = []
        
        i = 0
        while answer and i < len(s):
            if s[i] == '(':
                waiting.append(')')
            elif s[i] == '{':
                waiting.append('}')
            elif s[i] == '[':
                waiting.append(']')
            elif len(waiting) > 0:
                if s[i] != waiting[-1]:
                    answer = False
                else:
                    waiting.pop(-1)
            else:
                answer = False
            i += 1
        if len(waiting) > 0:
            answer = False
        
        return answer