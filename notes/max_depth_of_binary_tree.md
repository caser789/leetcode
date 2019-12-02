---
tags: [2019/08/13, application/tree/depth, data structure/queue, data structure/tree, leetcode/104, method/recursion, method/traversal/bfs, method/traversal/level]
title: Maximum Depth of Binary Tree
created: '2019-08-13T15:30:54.876Z'
modified: '2019-12-01T12:10:25.474Z'
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
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

### bfs

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
        if root is None:
            return 0
        
        q = [root]
        cnt = 0
        while q:
            cnt += 1
            nxt = []
            for e in q:
                if e.left:
                    nxt.append(e.left)
                if e.right:
                    nxt.append(e.right)
            q = nxt
        
        return cnt
```

## refs

* [lc](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
