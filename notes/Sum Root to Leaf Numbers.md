---
tags: [2019/11/28, application/tree/path, data structure/stack, data structure/tree, leetcode/129, method/traversal/dfs]
title: Sum Root to Leaf Numbers
created: '2019-11-28T08:23:43.116Z'
modified: '2019-12-02T14:26:00.567Z'
---

# Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.


## Solution

### dfs

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            return 0
        
        stack = [(root, root.val)]
        
        res = 0
        
        while stack:
            n, v = stack.pop()
            
            if n.left is None and n.right is None:
                res += v
                
            if n.left:
                stack.append((n.left, v*10+n.left.val))
            
            if n.right:
                stack.append((n.right, v*10+n.right.val))
        
        return res
```

## refs

* [lc](https://leetcode.com/problems/sum-root-to-leaf-numbers/)
