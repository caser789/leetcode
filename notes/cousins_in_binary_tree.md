---
tags: [2019/08/07, data structure/queue, data structure/tree, leetcode/993, method/traversal/bfs]
title: Cousins in Binary Tree
created: '2019-08-07T05:44:58.885Z'
modified: '2019-08-09T04:44:31.458Z'
---

# Cousins in Binary Tree

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.



### Example 1:

![pic](https://assets.leetcode.com/uploads/2019/02/12/q1248-01.png)

Input: root = [1,2,3,4], x = 4, y = 3
Output: false

### Example 2:

![pic](https://assets.leetcode.com/uploads/2019/02/12/q1248-02.png)

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

### Example 3:


![pic](https://assets.leetcode.com/uploads/2019/02/13/q1248-03.png)

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false


> The number of nodes in the tree will be between 2 and 100.
> Each node has a unique integer value from 1 to 100.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        queue = [root]
        n_to_parents = {}
        n_to_height = {}
        height = -1
        while queue:
            height += 1
            next_q = []
            for e in queue:
                n_to_height[e.val] = height
                if e.left:
                    next_q.append(e.left)
                    n_to_parents[e.left.val] = e.val
                if e.right:
                    next_q.append(e.right)
                    n_to_parents[e.right.val] = e.val
            queue = next_q
        if x not in n_to_height:
            return False
        if y not in n_to_height:
            return False
        if x not in n_to_parents:
            return False
        if y not in n_to_parents:
            return False
        return n_to_height[x] == n_to_height[y] and n_to_parents[x] != n_to_parents[y]
```
