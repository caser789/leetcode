---
tags: [2019/09/07, leetcode/429, TODO]
title: N-ary Tree Level Order Traversal
created: '2019-08-31T09:51:16.775Z'
modified: '2019-08-31T09:51:44.594Z'
---

# N-ary Tree Level Order Traversal

Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:

![pic](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]


## Note:

> The depth of the tree is at most 1000.
> The total number of nodes is at most 5000.

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
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

```
