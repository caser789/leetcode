---
tags: [2019/09/06, leetcode/590, TODO]
title: N-ary Tree Postorder Traversal
created: '2019-08-31T09:45:05.727Z'
modified: '2019-08-31T09:45:21.646Z'
---

# N-ary Tree Postorder Traversal

Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:

![pic](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)


Return its postorder traversal as: [5,6,3,2,4,1].


## Note:

Recursive solution is trivial, could you do it iteratively?

## Solution

```
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

```
