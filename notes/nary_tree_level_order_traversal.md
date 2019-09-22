---
tags: [2019/10/03, data structure/tree, leetcode/429, method/backtracking, method/traversal/bfs]
title: N-ary Tree Level Order Traversal
created: '2019-08-31T09:51:16.775Z'
modified: '2019-09-21T12:26:06.527Z'
---

# N-ary Tree Level Order Traversal

Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:

![pic](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

We should return its level order traversal:

```

[
     [1],
     [3,2,4],
     [5,6]
]
```


## Note:

> The depth of the tree is at most 1000.
> The total number of nodes is at most 5000.

## Solution

### bfs

```python
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
        res = []
        if root is None:
            return res

        q = [root]
        while q:
            tmp = []
            nxt = []
            for e in q:
                nxt.extend(e.children)
                tmp.append(e.val)
            q = nxt
            res.append(tmp)
        return res

```

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
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        def collect(node, level, res, count):
            if node is None:
                return
            if level < len(count):
                count[level] += 1
                res[level].append(node.val)
            else:
                count.append(1)
                res.append([node.val])
            for n in node.children:
                collect(n, level+1, res, count)

        res = []
        count = []
        collect(root, 0, res, count)
        return res

```

## schedule

* [x] 0 2019/09/07
* [x] 1 2019/09/08
* [x] 1 2019/09/11
* [x] 1 2019/09/18
* [ ] 1 2019/10/03

