---
tags: [BFS, depth, DFS, tree]
title: Maximum Depth of Binary Tree
created: '2019-08-06T15:20:22.138Z'
modified: '2019-08-06T15:21:04.281Z'
---

# Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

### Example:

```
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
```


## Solution

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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        if not root:
            return depth
        q = deque()
        q.append(root)
        while q:
            depth += 1
            for _ in range(len(q)):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return depth
```

### Recur

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        nodes = [root]
        depths = [1]
        max_depth = 1
        while nodes:
            n = nodes.pop()
            depth = depths.pop()

            if not n:
                max_depth = max(max_depth, depth)
            else:
                nodes.append(n.left)
                depths.append(depth+1)
                nodes.append(n.right)
                depths.append(depth+1)
        return max_depth
```

