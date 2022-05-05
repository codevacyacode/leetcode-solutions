# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:18:39 2022

@author: codevacyacode
"""
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
Runtime: 96 ms,
faster than 77.95% of Python3 online submissions 
for Remove Duplicates from Sorted Array.
Memory Usage: 15.5 MB, 
less than 96.64% of Python3 online submissions 
for Remove Duplicates from Sorted Array.
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range (1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        k += 1
        
        return k