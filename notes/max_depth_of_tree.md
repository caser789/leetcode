---
tags: [BFS, leetcode/559, queue, tree]
title: Maximum Depth of N-ary Tree
created: '2019-08-06T14:46:41.707Z'
modified: '2019-08-06T14:47:44.933Z'
---

# Maximum Depth of N-ary Tree

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:



![pic](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)


We should return its max depth, which is 3.




> The depth of the tree is at most 1000.
> The total number of nodes is at most 5000.

## Solution

```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root: return 0
        q = deque()
        q.append(root)
        depth = 0
        while q:
            depth += 1
            for i in range(len(q)):
                e = q.popleft()
                for c in e.children:
                    q.append(c)
        return depth
```
