---
tags: [2019/11/28, data structure/queue, data structure/tree, leetcode/199, method/traversal/level]
title: Binary Tree Right Side View
created: '2019-11-28T10:05:55.439Z'
modified: '2019-12-02T15:09:40.921Z'
---

# Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---


## Solution

### bfs with queue

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        res = []
        q = [root]
        while q:
            nxt = []
            v = None
            for e in q:
                v = e.val
                if e.left:
                    nxt.append(e.left)
                if e.right:
                    nxt.append(e.right)
            
            res.append(v)
            q = nxt
        return res
```

## refs

* [lc](https://leetcode.com/problems/binary-tree-right-side-view/)
