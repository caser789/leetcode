---
tags: [2019/11/04, leetcode/538]
title: Convert BST to Greater Tree
created: '2019-09-07T06:33:36.093Z'
modified: '2019-10-05T05:23:25.307Z'
---

# Convert BST to Greater Tree

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:

```
              5
            /   \
           2     13
```

Output: The root of a Greater Tree like this:

```
             18
            /   \
          20     13
```

## Solution

### inorder

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return

        vals = []

        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            vals.append(node.val)
            node = node.right

        n = len(vals)
        for i in range(n-2, -1, -1):
            vals[i] += vals[i+1]

        stack = []
        j = 0
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.val = vals[j]
            j += 1
            node = node.right
        return root
```

### recursive

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root
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
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        total = 0

        node = root
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            total += node.val
            node.val = total

            node = node.left
        return root
```

## schedule

* [x] 0 2019/09/08
* [x] 1 2019/09/09
* [x] 1 2019/09/12
* [x] 1 2019/09/19
* [x] 1 2019/10/04
* [ ] 1 2019/11/04
