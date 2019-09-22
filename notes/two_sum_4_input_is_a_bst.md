---
tags: [2019/10/04, leetcode/653]
title: Two Sum IV - Input is a BST
created: '2019-09-07T06:31:25.541Z'
modified: '2019-09-22T07:24:00.723Z'
---

# Two Sum IV - Input is a BST

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

### Example 1:

```

Input:
    5
   / \
  3   6
 / \   \
2   4   7
```

Target = 9

Output: True


### Example 2:

```
Input:
    5
   / \
  3   6
 / \   \
2   4   7
```

Target = 28

Output: False

## Solution

### bst

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """


        def find(node, v):
            if node is None:
                return False
            if node.val == v:
                return True
            if v < node.val:
                return find(node.left, v)
            return find(node.right, v)

        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if k-node.val != node.val and find(root, k-node.val):
                return True
            node = node.right
        return False
```

### recur +set

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def find(node, k, ss):
            if node is None:
                return False
            if k - node.val in ss:
                return True
            ss.add(node.val)
            return find(node.left, k, ss) or find(node.right, k, ss)

        s = set()
        return find(root, k, s)
```

### 2 pointers

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        lst = []

        stack = []
        node = root
        n = 0
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            lst.append(node.val)
            n += 1
            node = node.right

        i = 0
        j = n - 1
        while i < j:
            s = lst[i] + lst[j]
            if s == k:
                return True
            elif s < k:
                i += 1
            else:
                j -= 1
        return False
```

## schedule

* [x] 0 2019/09/08
* [x] 1 2019/09/09
* [x] 1 2019/09/12
* [x] 1 2019/09/19
* [ ] 1 2019/10/04
