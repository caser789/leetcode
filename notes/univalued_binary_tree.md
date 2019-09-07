---
tags: [2019/09/08, data structure/tree, leetcode/965, method/recursion, method/traversal/dfs]
title: Univalued Binary Tree
created: '2019-08-31T09:46:44.066Z'
modified: '2019-09-07T05:14:25.604Z'
---

# Univalued Binary Tree


A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.



Example 1:

![pic](https://assets.leetcode.com/uploads/2018/12/28/unival_bst_1.png)

Input: [1,1,1,1,1,null,1]
Output: true
Example 2:


![pic](https://assets.leetcode.com/uploads/2018/12/28/unival_bst_2.png)

Input: [2,2,2,5,2]
Output: false

## Note:

The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].

## Solution

### dfs

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        v = root.val
        stack = [root]
        while stack:
            n = stack.pop()
            if n.val != v:
                return False
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)
        return True
```
### recursive

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        left_correct = (
            not root.left or
            root.val == root.left.val and
            self.isUnivalTree(root.left)
        )
        right_correct = (
            not root.right or
            root.val == root.right.val and
            self.isUnivalTree(root.right)
        )
        return left_correct and right_correct
```

## schedule

* [x] 0 2019/09/07
* [ ] 1 2019/09/08
