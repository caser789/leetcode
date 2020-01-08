---
tags: [2019/11/27, application/tree/zigzag, data structure/queue, data structure/tree, leetcode/103, method/traversal/level]
title: Binary Tree Zigzag Level Order Traversal
created: '2019-11-27T14:00:25.832Z'
modified: '2019-12-02T15:10:11.141Z'
---

# Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return
        
        q = [root]
        res = []
        direction = 1
        
        while q:
            nxt = []
            tmp = []
            for e in q:
                tmp.append(e.val)
                if e.left:
                    nxt.append(e.left)
                if e.right:
                    nxt.append(e.right)
            
            q = nxt
            res.append(tmp[::direction])
            direction *= -1
        
        return res
            
                
```

## refs

* [lc](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

