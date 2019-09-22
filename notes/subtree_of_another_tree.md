---
tags: [2019/10/06, leetcode/572]
title: Subtree of Another Tree
created: '2019-09-07T06:58:16.003Z'
modified: '2019-09-22T10:32:57.333Z'
---

# Subtree of Another Tree

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

### Example 1:

Given tree s:

```
     3
    / \
   4   5
  / \
 1   2
```
Given tree t:

```
   4
  / \
 1   2
```
Return true, because t has the same structure and node values with a subtree of s.

### Example 2:

Given tree s:

```
     3
    / \
   4   5
  / \
 1   2
    /
   0
```
Given tree t:

```
   4
  / \
 1   2
```

Return false.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """


        def collect(node, kv):
            if node in kv:
                return kv[node]
            s = '{}>{}<{}'.format(collect(node.left, kv), node.val, collect(node.right, kv))
            kv[node] = s
            return s
        kv = {None: 'None'}
        collect(s, kv)
        kv2 = {None: 'None'}
        s = collect(t, kv2)
        return s in kv.values()
```

## schedule

* [x] 0 2019/09/10
* [x] 1 2019/09/11
* [x] 1 2019/09/14
* [x] 1 2019/09/21
* [ ] 1 2019/10/06
