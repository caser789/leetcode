---
tags: [2019/11/16, data structure/queue, data structure/tree, leetcode/513, method/traversal/level]
title: Find Bottom Left Tree Value
created: '2019-11-16T14:26:31.450Z'
modified: '2019-12-03T13:22:57.985Z'
---

# Find Bottom Left Tree Value

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.


## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = [root]
        v = root.val
        
        while q:
            nxt = []
            v = q[0].val
            for e in q:
                if e.left:
                    nxt.append(e.left)
                if e.right:
                    nxt.append(e.right)
            q = nxt
        
        return v
                
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
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            return
        
        max_depth =  0
        res = root.val
        
        stack = [(root, 0)]
        
        while stack:
            n, level = stack.pop()
            
            if level > max_depth:
                max_depth = level
                res = n.val
            
            if n.right:
                stack.append((n.right, level+1))
            
            if n.left:
                stack.append((n.left, level+1))
        
        return res
```

## refs

* [lc](https://leetcode.com/problems/find-bottom-left-tree-value/)

