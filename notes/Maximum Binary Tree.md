---
deleted: true
tags: [2019/11/14]
title: Maximum Binary Tree
created: '2019-11-14T01:15:08.018Z'
modified: '2019-12-08T10:55:37.816Z'
---

# Maximum Binary Tree

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
Note:
The size of the given array will be in the range [1,1000].


## Solution

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        n = len(nums)
        if n == 1:
            return TreeNode(nums[0])
        
        
        i = 0
        for j in range(1, len(nums)):
            if nums[j] > nums[i]:
                i = j
        
        node = TreeNode(nums[i])
        node.left = self.constructMaximumBinaryTree(nums[:i])
        node.right = self.constructMaximumBinaryTree(nums[i+1:])
        return node
```

## refs

* [lc](https://leetcode.com/problems/maximum-binary-tree/)
