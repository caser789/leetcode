---
tags: [2019/11/29, leetcode/515, method/traversal/level]
title: Find Largest Value in Each Tree Row
created: '2019-11-29T03:25:20.133Z'
modified: '2019-12-03T13:25:39.744Z'
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

### dfs

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
        
        stack = [(root, 0)]
        res = []
        while stack:
            n, level = stack.pop()
            if len(res) == level:
                res.append(n.val)
            elif n.val > res[level]:
                res[level] = n.val
            
            if n.left:
                stack.append((n.left, level+1))
            
            if n.right:
                stack.append((n.right, level+1))
        
        return res
            
```

## refs

* [lc](https://leetcode.com/problems/find-largest-value-in-each-tree-row/)
