---
tags: [2019/11/30, data structure/heap, data structure/tree-in-array, data structure/tree/complete, leetcode/958]
title: Check Completeness of a Binary Tree
created: '2019-11-30T09:19:39.919Z'
modified: '2019-12-07T09:03:31.171Z'
---

# Check Completeness of a Binary Tree

Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

Example 1:

![pic](https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-1.png)

Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:

![pic](https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-2.png)

Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
 
Note:

The tree will have between 1 and 100 nodes.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes = [(root, 1)]
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node.left:
                nodes.append((node.left, 2*v))
            if node.right:
                nodes.append((node.right, 2*v+1))

        return nodes[-1][1] == len(nodes)
```

## refs

* [lc](https://leetcode.com/problems/check-completeness-of-a-binary-tree/)
