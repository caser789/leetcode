---
tags: [2019/08/09, data structure/stack, data structure/tree, leetcode/144, method/recursion, method/traversal/preorder]
title: Binary Tree Preorder Traversal
created: '2019-08-09T09:47:59.259Z'
modified: '2019-11-28T08:28:23.021Z'
---

# Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.

### Example:

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
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
    def preorderTraversal(self, root):
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
                res.append(node.val)
                node = node.left
            node = stack.pop()
            node = node.right
        return res
```

### recur

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root is None:
            return []
        
        res = []
        
        def helper(node):
            if node is None:
                return
            
            res.append(node.val)
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return res
```

## refs

* [lc](https://leetcode.com/problems/binary-tree-preorder-traversal/)

