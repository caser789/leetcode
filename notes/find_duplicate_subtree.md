---
tags: [application/tree/duplicate, data structure/map, data structure/tree]
title: Find Duplicate Subtrees
created: '2019-08-01T05:44:17.097Z'
modified: '2019-08-09T04:40:02.542Z'
---

# Find Duplicate Subtrees


Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

### Example 1:

```
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4

Therefore, you need to return above trees' root in the form of a list.
```


## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if not root:
            return []

        stack = []
        stack.append(root)
        store = {}
        while stack:
            n = stack.pop()
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)
            k = self.serialize_tree(n)
            store.setdefault(k, [])
            store[k].append(n)
        res = []
        for k, v in store.items():
            if len(v) > 1:
                res.append(v[0])
        return res

    def serialize_tree(self, node):
        if not node:
            return '#'
        return '({}<{}>{})'.format(self.serialize_tree(node.left), node.val, self.serialize_tree(node.right))
```
