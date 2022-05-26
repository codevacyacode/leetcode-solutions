# -*- coding: utf-8 -*-
"""
Created on Wed May 25 19:26:39 2022

@author: codevacyacode

https://leetcode.com/problems/binary-tree-inorder-traversal/

Runtime: 50 ms, faster than 28.32% of Python3 online submissions
for Binary Tree Inorder Traversal.
Memory Usage: 13.9 MB, less than 60.34% of Python3 online submissions 
for Binary Tree Inorder Traversal.
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        route = []
        worried_parents = []
        
        while root:
            while root.left != None:
                worried_parents.append(root)
                tmp = root.left
                root.left = None
                root = tmp
            route.append(root.val)
            if root.right != None:
                tmp = root.right
                root.right = None
                root = tmp
            elif len(worried_parents) > 0:
                root = worried_parents[-1]
                worried_parents.pop(-1)
            else:
                root = None
           
        return route