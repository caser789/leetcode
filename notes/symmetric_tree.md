---
tags: [2019/08/07, BFS, leetcode/101]
title: Symmetric Tree
created: '2019-08-07T14:22:53.723Z'
modified: '2019-08-07T14:23:41.966Z'
---

# Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```


But the following [1,2,2,null,3,null,3] is not:

```
    1
   / \
  2   2
   \   \
   3    3
```


> Bonus points if you could solve it both recursively and iteratively.

## Solution


```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        q = [root]
        while q:
            next_q = []
            for i in range(len(q)):
                left_node = q[i]
                right_node = q[len(q)-i-1]
                if left_node.val != right_node.val:
                    return False

                if left_node.left:
                    if not right_node.right:
                        return False
                    if left_node.left.val != right_node.right.val:
                        return False
                else:
                    if right_node.right:
                        return False

                if left_node.right:
                    if not right_node.left:
                        return False
                    if right_node.left.val != left_node.right.val:
                        return False
                else:
                    if right_node.left:
                        return False

                if left_node.left:
                    next_q.append(left_node.left)
                if left_node.right:
                    next_q.append(left_node.right)
            q = next_q
        return True
```
