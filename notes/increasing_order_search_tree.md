---
tags: [2019/08/07, data structure/tree, method/traversal/inorder]
title: Increasing Order Search Tree
created: '2019-08-07T15:39:08.211Z'
modified: '2019-08-09T09:34:30.818Z'
---

# Increasing Order Search Tree

Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

### Example 1:

```
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9
```

> The number of nodes in the given tree will be between 1 and 100.
> Each node will have a unique integer value from 0 to 1000.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        new = head = TreeNode(0)
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            new.right = root
            new = new.right
            root = root.right
            new.left = None
        return head.right
```
