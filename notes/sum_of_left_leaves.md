---
tags: [2019/11/08, application/tree/leaf, leetcode/404, method/recursion]
title: Sum of Left Leaves
created: '2019-09-07T06:43:00.528Z'
modified: '2019-12-09T13:31:19.868Z'
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

### is_left

* 遍历每个节点， 找到所有左叶子节点，把它们的值加起来
* 如果一个节点没有左右子书，并且这个节点是它的父节点的左子树，它是一个左叶子节点

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
        stack = [(root, False)]
        while stack:
            n, is_left = stack.pop()
            if n.left is None and n.right is None and is_left:
                res += n.val
            
            if n.left:
                stack.append((n.left, True))
            
            if n.right:
                stack.append((n.right, False))
            
        
        return res
```


## schedule

* [x] 0 2019/09/08
* [x] 1 2019/09/09
* [x] 1 2019/09/12
* [x] 1 2019/09/13
* [x] 1 2019/09/16
* [x] 1 2019/09/23
* [x] 1 2019/10/08
* [ ] 1 2019/11/08
