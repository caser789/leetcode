---
favorited: true
tags: [2019/11/30, application/flip-tree, data structure/tree, leetcode/971, method/traversal/dfs]
title: Flip Binary Tree To Match Preorder Traversal
created: '2019-11-30T10:00:53.894Z'
modified: '2019-11-30T10:06:40.124Z'
---

# Flip Binary Tree To Match Preorder Traversal

Given a binary tree with N nodes, each node has a different value from {1, ..., N}.

A node in this binary tree can be flipped by swapping the left child and the right child of that node.

Consider the sequence of N values reported by a preorder traversal starting from the root.  Call such a sequence of N values the voyage of the tree.

(Recall that a preorder traversal of a node means we report the current node's value, then preorder-traverse the left child, then preorder-traverse the right child.)

Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage we are given.

If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.

If we cannot do so, then return the list [-1].

 

Example 1:

![pic](https://assets.leetcode.com/uploads/2019/01/02/1219-01.png)

Input: root = [1,2], voyage = [2,1]
Output: [-1]
Example 2:

![pic](https://assets.leetcode.com/uploads/2019/01/02/1219-02.png)

Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]
Example 3:

![pic](https://assets.leetcode.com/uploads/2019/01/02/1219-02.png)

Input: root = [1,2,3], voyage = [1,2,3]
Output: []
 

Note:

1 <= N <= 100
Accepted

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        self.i = 0
        self.flipped = []
        
        def dfs(node):
            if node is None:
                return
            
            if node.val != voyage[self.i]:
                self.flipped = [-1]
                return
            
            self.i += 1
            
            if (self.i < len(voyage) and node.left and node.left.val != voyage[self.i]):
                self.flipped.append(node.val)
                dfs(node.right)
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        
        if self.flipped and self.flipped[0] == -1:
            self.flipped = [-1]
        return self.flipped
```

## refs

* [lc](https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/)
