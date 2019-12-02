---
tags: [2019/08/09, data structure/BST, data structure/tree, leetcode/108, method/recursion]
title: Convert Sorted Array to Binary Search Tree
created: '2019-08-09T10:23:42.544Z'
modified: '2019-11-28T04:05:49.981Z'
---

# Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

### Example:

```
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
```

## Solution

```python
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        return self.get(nums, 0, len(nums)-1)

    def get(self, nums, lo, hi):
        if lo > hi:
            return
        mi = (lo + hi) / 2
        n = TreeNode(nums[mi])
        n.left = self.get(nums, lo, mi-1)
        n.right = self.get(nums, mi+1, hi)
        return n
```

## refs

* [lc](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)
