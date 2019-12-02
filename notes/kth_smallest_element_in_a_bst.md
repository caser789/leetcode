---
tags: [2019/08/09, data structure/bst, data structure/tree, leetcode/230, method/traversal/inorder]
title: Kth Smallest Element in a BST
created: '2019-08-09T09:41:18.677Z'
modified: '2019-12-01T08:31:36.785Z'
---

# Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

> You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

### Example 1:

```
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
```


### Example 2:

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
```

## Solution

```python
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return

        stack = []
        node = root
        i = 0
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            i += 1
            if i == k:
                return node.val
            node = node.right



_1 = TreeNode(1)
_2 = TreeNode(2)
_3 = TreeNode(3)
_4 = TreeNode(4)
_5 = TreeNode(5)
_6 = TreeNode(6)

_5.left = _3
_5.right = _6
_3.left = _2
_3.right = _4
_2.left = _1

Solution().kthSmallest(_5, 1)
```

## refs

* [lc](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
