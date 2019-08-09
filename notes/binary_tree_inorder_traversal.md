---
tags: [2019/08/09, data structure/tree, leetcode/94]
title: Binary Tree Inorder Traversal
created: '2019-08-09T09:30:54.852Z'
modified: '2019-08-09T15:05:40.292Z'
---

#  Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

### Example:

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        stack = []
        node = root
        res = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
```
