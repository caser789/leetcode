---
tags: [2019/11/29]
title: Find Largest Value in Each Tree Row
created: '2019-11-29T03:25:20.133Z'
modified: '2019-11-29T03:26:00.396Z'
---

#  Find Largest Value in Each Tree Row

You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        res = []
        
        q = [root]
        while q:
            nxt = []
            v = q[0].val
            for e in q:
                v = max(v, e.val)
                if e.left:
                    nxt.append(e.left)
                if e.right:
                    nxt.append(e.right)
            q = nxt
            res.append(v)
        return res
```

## refs

* [lc](https://leetcode.com/problems/find-largest-value-in-each-tree-row/)
