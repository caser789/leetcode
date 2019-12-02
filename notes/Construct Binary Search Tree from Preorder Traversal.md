---
deleted: true
tags: [2019/11/14]
title: Construct Binary Search Tree from Preorder Traversal
created: '2019-11-14T01:23:59.133Z'
modified: '2019-12-01T08:47:52.197Z'
---

# Construct Binary Search Tree from Preorder Traversal

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

 

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 ![pic](https://assets.leetcode.com/uploads/2019/03/06/1266.png)

Note: 

1 <= preorder.length <= 100
The values of preorder are distinct.

## Solution

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        n = len(preorder)
        if not n:
            return None
        if n == 1:
            return TreeNode(preorder[0])
        
        
        j = 1
        while j < n and preorder[j] < preorder[0]:
            j += 1
        
        node = TreeNode(preorder[0])
        node.left = self.bstFromPreorder(preorder[1:j])
        node.right = self.bstFromPreorder(preorder[j:])
        return node
```

## refs

* [lc](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)
