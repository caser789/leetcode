---
tags: [2019/11/06, leetcode/563]
title: Binary Tree Tilt
created: '2019-09-07T06:48:19.230Z'
modified: '2019-10-07T05:31:35.692Z'
---

# Binary Tree Tilt

Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

### Example:
Input:

```
         1
       /   \
      2     3
```

Output: 1

Explanation:

Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1

### Note:

The sum of node values in any subtree won't exceed the range of 32-bit integer.
All the tilt values won't exceed the range of 32-bit integer.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.t = 0
        def traverse(node):
            if node is None:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            self.t += abs(left - right)
            return left + right + node.val
        traverse(root)
        return self.t
```

## schedule

* [x] 0 2019/09/09
* [x] 1 2019/09/10
* [x] 1 2019/09/13
* [x] 1 2019/09/21
* [x] 1 2019/10/06
* [ ] 1 2019/11/06
