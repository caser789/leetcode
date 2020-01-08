---
tags: [2019/08/07, data structure/queue, data structure/tree, leetcode/107, method/traversal/level]
title: Binary Tree Level Order Traversal II
created: '2019-08-07T14:05:01.221Z'
modified: '2019-12-02T15:09:28.337Z'
---

# Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

### For example:

```
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
```

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = [root]
        res = []
        while q:
            next_q = []
            lst = []
            for e in q:
                lst.append(e.val)
                if e.left:
                    next_q.append(e.left)
                if e.right:
                    next_q.append(e.right)
            q = next_q
            res.append(lst)
        return res[::-1]
```
