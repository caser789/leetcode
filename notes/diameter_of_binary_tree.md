---
tags: [2019/10/04, application/tree/height, data structure/tree, leetcode/543]
title: Diameter of Binary Tree
created: '2019-09-07T06:46:04.327Z'
modified: '2019-09-22T04:44:08.618Z'
---

# Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

### Example:

Given a binary tree

```
          1
         / \
        2   3
       / \
      4   5
```

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.res = 1
        def depth(node):
            if node is None:
                return 0

            L = depth(node.left)
            R = depth(node.right)
            self.res = max(self.res, L+R+1)
            return max(L, R) + 1
        depth(root)
        return self.res - 1
```

## schedule

* [x] 0 2019/09/08
* [x] 1 2019/09/09
* [x] 1 2019/09/12
* [x] 1 2019/09/19
* [ ] 1 2019/10/04
