---
tags: [2019/08/17, data structure/BST, leetcode/938, method/traversal/inorder]
title: Range Sum of BST
created: '2019-08-17T03:41:32.348Z'
modified: '2019-08-17T03:48:56.175Z'
---

# Range Sum of BST

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

### Example 1:

```
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
```

### Example 2:

```
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
```


> The number of nodes in the tree is at most 10000.
> The final answer is guaranteed to be less than 2^31.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0

        curr = root
        stack = []
        done = False
        while curr or stack and not done:
            done = True
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if curr.val >= L and curr.val <= R:
                res += curr.val
            if curr.val <= R:
                done = False
            curr = curr.right
        return res
```
