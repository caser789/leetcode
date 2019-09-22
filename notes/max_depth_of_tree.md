---
tags: [2019/10/03, data structure/queue, data structure/stack, data structure/tree, leetcode/559, method/recursion, method/traversal/bfs, method/traversal/dfs]
title: Maximum Depth of N-ary Tree
created: '2019-08-06T14:46:41.707Z'
modified: '2019-09-21T12:07:23.765Z'
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

### BFS Iter

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

### DFS Iter

```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root: return 0

        nodes = [root]
        depths = [1]
        max_depth = 1
        while nodes:
            n = nodes.pop()
            depth  = depths.pop()

            if not n.children:
                max_depth = max(max_depth, depth)

            for c in n.children:
                nodes.append(c)
                depths.append(depth+1)
        return max_depth
```


### DFS Recur

```python
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1
        return max(self.maxDepth(c) for c in root.children) + 1
```

## schedule

* [x] 0 2019/09/07
* [x] 1 2019/09/08
* [x] 1 2019/09/11
* [x] 1 2019/09/18
* [ ] 1 2019/10/03
