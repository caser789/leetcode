---
tags: [2019/11/05, application/tree/lca, data structure/bst, data structure/tree, leetcode/235, method/recursion]
title: Lowest Common Ancestor of a Binary Search Tree
created: '2019-09-07T06:52:25.374Z'
modified: '2019-12-04T12:35:05.494Z'
---

# Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]


 ![pic](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

### Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6

Explanation: The LCA of nodes 2 and 8 is 6.

### Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.


## Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.

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
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_val = p.val
        q_val = q.val
        node = root
        while node:
            parent_val = node.val
            if p_val > parent_val and q_val > parent_val:
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                node = node.left
            else:
                return node
```

### recur

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent_val = root.val
        p_val = p.val
        q_val = q.val
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
```

## schedule

* [x] 0 2019/09/09
* [x] 1 2019/09/10
* [x] 1 2019/09/13
* [x] 1 2019/09/20
* [x] 1 2019/10/05
* [ ] 1 2019/11/05

## refs

* [lc](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

