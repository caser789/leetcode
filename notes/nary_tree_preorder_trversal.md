---
tags: [2019/10/28, data structure/stack, data structure/tree/n-ary, leetcode/589, method/recursion, method/traversal/preorder]
title: N-ary Tree Preorder Traversal
created: '2019-08-31T09:43:30.048Z'
modified: '2019-12-01T11:09:38.729Z'
---

# N-ary Tree Preorder Traversal

Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:

![pic](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)


Return its preorder traversal as: [1,3,5,6,2,4].


## Note:

Recursive solution is trivial, could you do it iteratively?

## Solution

### recursive

```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        lst = []
        def get(node):
            if node is None:
                return
            lst.append(node.val)
            for c in node.children:
                get(c)

        get(root)
        return lst
```

### iter

```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []

        res = []
        stack = [root]
        while stack:
            n = stack.pop()
            res.append(n.val)
            for c in n.children[::-1]:
                if c:
                    stack.append(c)

        return res
```

## schedule

* [x] 0 2019/09/06
* [x] 1 2019/09/07
* [x] 1 2019/09/08
* [x] 1 2019/09/11
* [x] 1 2019/09/18
* [x] 1 2019/10/03
* [x] 1 2019/10/06
* [x] 1 2019/10/13
* [ ] 1 2019/10/28

## refs

* [lc](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)
