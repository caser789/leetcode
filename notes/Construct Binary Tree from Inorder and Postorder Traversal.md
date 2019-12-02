---
tags: [2019/11/28, leetcode/106, method/recursion, method/traversal/inorder]
title: Construct Binary Tree from Inorder and Postorder Traversal
created: '2019-11-28T03:50:23.001Z'
modified: '2019-12-01T08:48:10.272Z'
---

# Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        n = len(inorder)
        
        v_to_i = {}
        for i, v in enumerate(inorder):
            v_to_i[v] = i
        
        def build(i, j, m, n):
            if j < i:
                return
            
            v = postorder[n]
            k = v_to_i[v]
            node = TreeNode(v)
            length = k - i
            node.left = build(i, k-1, m, m+length-1)
            node.right = build(k+1, j, m+length, n-1)
            return node
        
        
        return build(0, n-1, 0, n-1)
```

## refs

* [lc](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
