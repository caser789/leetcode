---
tags: [2019/08/06, application/tree/depth, data structure/queue, data structure/stack, data structure/tree, leetcode/111, method/recursion, method/traversal/bfs, method/traversal/dfs, method/traversal/level]
title: Minimum Depth of Binary Tree
created: '2019-08-06T15:37:26.470Z'
modified: '2019-12-01T12:10:38.672Z'
---

# Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

### Example:

```
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
```

## Solution

### Recur

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        if root.left:
            return 1 + self.minDepth(root.left)
        return 1 + self.minDepth(root.right)
```


### DFS

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        min_depth = 10000
        nodes = [root]
        depths = [1]
        while nodes:
            n = nodes.pop()
            depth = depths.pop()

            if not n.left and not n.right:
                min_depth = min(min_depth, depth)
            if n.left:
                nodes.append(n.left)
                depths.append(depth+1)
            if n.right:
                nodes.append(n.right)
                depths.append(depth+1)
        return min_depth
```

### BFS

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth = 0
        q = deque()
        q.append(root)
        while q:
            depth += 1
            for _ in range(len(q)):
                n = q.popleft()
                if n.left is None and n.right is None:
                    return depth
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return depth
```

## refs

* [lc](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

