---
tags: [2019/11/28, application/tree/bubble, data structure/tree, leetcode/124, method/recursion, TODO]
title: Binary Tree Maximum Path Sum
created: '2019-11-28T08:18:51.154Z'
modified: '2019-12-02T14:26:38.934Z'
---

# Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42


## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        self.max = float('-inf')
        
        def helper(node):
            if node is None:
                return 0
            
            left = helper(node.left)
            left = max(left, 0)
            right = helper(node.right)
            right = max(right, 0)
            
            res = left + right + node.val
            self.max = max(self.max, res)
            
            return max(left, right) + node.val
        
        helper(root)
        return self.max
            
```

## refs

* [lc](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
