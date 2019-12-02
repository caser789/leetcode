---
tags: [2019/11/04, data structure/bst, data structure/tree, leetcode/530, method/recursion, method/traversal/inorder]
title: Minimum Absolute Difference in BST
created: '2019-09-07T06:41:02.230Z'
modified: '2019-12-01T11:30:29.138Z'
---

# Minimum Absolute Difference in BST

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

### Example:

Input:

```
   1
    \
     3
    /
   2
```

Output:

1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

## Solution


```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        val = 99999999
        prev = None

        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if prev is None:
                prev = node.val
            else:
                val = min(val, node.val - prev)
                prev = node.val

            node = node.right

        return val
```

### recur

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.res = float('inf')
        self.prev = None
        
        def helper(node):
            if node is None:
                return
            
            helper(node.left)
            if self.prev is not None:
                self.res = min(self.res, node.val - self.prev)
            self.prev = node.val
            
            helper(node.right)
        
        helper(root)
        return self.res
```

## schedule

* [x] 0 2019/09/08
* [x] 1 2019/09/09
* [x] 1 2019/09/12
* [x] 1 2019/09/19
* [x] 1 2019/10/04
* [ ] 1 2019/11/04

## refs

* [lc](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)
