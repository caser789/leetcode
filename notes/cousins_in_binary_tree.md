---
tags: [2019/08/07, data structure/queue, data structure/tree, leetcode/993, method/recursion, method/traversal/bfs, method/traversal/dfs/parent]
title: Cousins in Binary Tree
created: '2019-08-07T05:44:58.885Z'
modified: '2019-12-01T12:05:47.901Z'
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

### dfs

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
        
        x_parent_level = []
        y_parent_level = []
        
        def find(node, parent=None, level=0):
            if node is None:
                return
            
            if node.val == x:
                x_parent_level.extend([parent, level])
            if node.val == y:
                y_parent_level.extend([parent, level])
            
            find(node.left, node, level+1)
            find(node.right, node, level+1)
        
        
        find(root)
        
        return x_parent_level and y_parent_level and x_parent_level[1] == y_parent_level[1] and x_parent_level[0] is not y_parent_level[0]
```

## refs

* [lc](https://leetcode.com/problems/cousins-in-binary-tree/)
