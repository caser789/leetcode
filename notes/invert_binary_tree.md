---
tags: [2019/09/18, data structure/tree, leetcode/226, method/traversal/bfs]
title: Invert Binary Tree
created: '2019-08-31T09:54:21.169Z'
modified: '2019-09-11T05:56:23.569Z'
---

# Invert Binary Tree

Invert a binary tree.

### Example:

```
Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

## Trivia:


Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

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
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
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
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        stack = [root]
        while stack:
            n = stack.pop()
            n.left, n.right = n.right, n.left
            if n.left: stack.append(n.left)
            if n.right: stack.append(n.right)
        return root


```


## schedule

* [x] 0 2019/09/07
* [x] 1 2019/09/08
* [x] 1 2019/09/11
* [ ] 1 2019/09/18
