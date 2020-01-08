---
tags: [2019/11/27, data structure/queue, data structure/tree, leetcode/102, method/traversal/level]
title: Binary Tree Level Order Traversal
created: '2019-11-27T13:49:44.470Z'
modified: '2019-12-02T15:09:21.808Z'
---

# Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]


## Solution

### bfs

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        res = []
        q = [root]
        while q:
            nxt = []
            tmp = []
            
            for e in q:
                tmp.append(e.val)
                if e.left:
                    nxt.append(e.left)
                if e.right:
                    nxt.append(e.right)
            
            res.append(tmp)
            q = nxt
        return res
```

## refs

* [lc](https://leetcode.com/problems/binary-tree-level-order-traversal/)
