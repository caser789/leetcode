---
tags: [2019/09/07, leetcode/617]
title: Merge Two Binary Trees
created: '2019-08-31T09:39:47.220Z'
modified: '2019-09-06T13:44:01.339Z'
---

# Merge Two Binary Trees

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

### Example 1:

```
Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
```


Note: The merging process must start from the root nodes of both trees.

## Solution

### recursive

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None: return t2
        if t2 is None: return t1
        n = TreeNode(t1.val+t2.val)
        n.left = self.mergeTrees(t1.left, t2.left)
        n.right = self.mergeTrees(t1.right, t2.right)
        return n
```


### itertive

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        stack = [[t1, t2]]
        while stack:
            a, b = stack.pop()
            if b is None:
                continue
            a.val += b.val
            if a.left is None:
                a.left = b.left
            else:
                stack.append([a.left, b.left])
            if a.right is None:
                a.right = b.right
            else:
                stack.append([a.right, b.right])

        return t1

```

## schedule

* [x] 0 2019/09/06
* [ ] 1 2019/09/07
