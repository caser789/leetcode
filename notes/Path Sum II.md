---
tags: [2019/11/28, application/path-sum, data structure/stack, data structure/tree, leetcode/113, method/backtrack, method/traversal/dfs]
title: Path Sum II
created: '2019-11-28T06:18:40.438Z'
modified: '2019-11-28T06:25:13.128Z'
---

# Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        res = []
        tmp = []
        
        def find(node, s):
            if node is None:
                return
            
            if node.left is None and node.right is None and s + node.val == sum:
                tmp.append(node.val)
                res.append(tmp[:])
                tmp.pop()
                return
            
            for n in [node.left, node.right]:
                if not n: continue
                tmp.append(node.val)
                find(n, s+node.val)
                tmp.pop()
            
        
        find(root, 0)
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        stack = [(root, root.val, [root.val])]
        res = []
        
        
        while stack:
            n, s, tmp = stack.pop()
            
            if n.left is None and n.right is None and s == sum:
                res.append(tmp)
            
            if n.left:
                stack.append((n.left, s+n.left.val, tmp + [n.left.val]))
            
            if n.right:
                stack.append((n.right, s+n.right.val, tmp+[n.right.val]))
        
        return res
```

## refs

* [lc](https://leetcode.com/problems/path-sum-ii/)
