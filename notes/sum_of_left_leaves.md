---
tags: [2019/10/08, leetcode/404]
title: Sum of Left Leaves
created: '2019-09-07T06:43:00.528Z'
modified: '2019-09-23T14:38:45.996Z'
---

# Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

```
    3
   / \
  9  20
    /  \
   15   7
```

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

## Solution

### recursive

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        res = 0
        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                res += root.left.val
            else:
                res += self.sumOfLeftLeaves(root.left)
        res += self.sumOfLeftLeaves(root.right)
        return res
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
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        stack = [root]
        res = 0
        while stack:
            n = stack.pop()

            if n.left:
                if n.left.left is None and n.left.right is None:
                    res += n.left.val
                else:
                    stack.append(n.left)

            if n.right:
                if n.right.left or n.right.right:
                    stack.append(n.right)
        return res

```


## schedule

* [x] 0 2019/09/08
* [x] 1 2019/09/09
* [x] 1 2019/09/12
* [x] 1 2019/09/13
* [x] 1 2019/09/16
* [x] 1 2019/09/23
* [ ] 1 2019/10/08
