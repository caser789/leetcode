---
tags: [2019/11/04, leetcode/1022]
title: Sum of Root To Leaf Binary Numbers
created: '2019-09-07T06:29:00.205Z'
modified: '2019-10-06T10:35:14.112Z'
---

# Sum of Root To Leaf Binary Numbers

Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.



### Example 1:

![pic](https://assets.leetcode.com/uploads/2019/04/04/sum-of-root-to-leaf-binary-numbers.png)

Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22


## Note:

The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.

## Solution

### iter

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.s = 0
        def _sum(node, _s):
            if node is None:
                return
            _s = _s*2 + node.val

            if node.left is None and node.right is None:
                self.s += _s
            _sum(node.left, _s)
            _sum(node.right,  _s)

        _sum(root,  0)
        return self.s
```

### iter

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        stack = [(root, 0)]
        s = 0
        while stack:
            n, _s = stack.pop()
            _s = _s*2 + n.val

            if n.left is None and n.right is None:
                s += _s

            if n.left:
                stack.append((n.left, _s))
            if n.right:
                stack.append((n.right, _s))
        return s

```

## schedule

* [x] 0 2019/09/08
* [x] 1 2019/09/09
* [x] 1 2019/09/12
* [x] 1 2019/09/19
* [x] 1 2019/10/04
* [ ] 1 2019/11/04
