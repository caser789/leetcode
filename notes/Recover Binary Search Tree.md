---
tags: [2019/11/27, data structure/BST, data structure/tree, leetcode/99, method/traversal/inorder]
title: Recover Binary Search Tree
created: '2019-11-27T10:52:27.974Z'
modified: '2019-12-01T08:00:09.159Z'
---

# Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

### Example 1:

Input: [1,3,null,null,2]

```
   1
  /
 3
  \
   2
```

Output: [3,1,null,null,2]

```
   3
  /
 1
  \
   2
```

### Example 2:

Input: [3,1,4,null,null,2]

```
  3
 / \
1   4
   /
  2
```

Output: [2,1,4,null,null,3]

```
  2
 / \
1   4
   /
  3
```

### Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        
        6 3 4 5 2
        """
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))
        
        def helper(node):
            if node is None:
                return
            
            helper(node.left)
            
            if self.first is None and self.prev.val >= node.val:
                self.first = self.prev
            
            if self.first is not None and self.prev.val >= node.val:
                self.second = node
            
            self.prev = node
            
            helper(node.right)
        
        helper(root)
        self.first.val, self.second.val = self.second.val, self.first.val
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
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        
        first = None
        second = None
        prev = TreeNode(float('-inf'))
        
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if first is None and prev.val >= root.val:
                first = prev
            
            if first is not None and prev.val >= root.val:
                second = root
            prev = root
            root = root.right
        
        first.val, second.val = second.val, first.val
```

## refs

* [lc](https://leetcode.com/problems/recover-binary-search-tree/)
