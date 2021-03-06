---
tags: [2019/08/08, application/tree/compare, data structure/tree, leetcode/872, method/recursion, method/traversal/dfs]
title: Leaf-Similar Trees
created: '2019-08-08T15:09:36.423Z'
modified: '2019-12-03T01:35:09.243Z'
---

# Leaf-Similar Trees

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.


![pic](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png)

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.




> Both of the given trees will have between 1 and 100 nodes.


## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.calc(root1) == self.calc(root2)

    def calc(self, node):
        res = []
        if not node:
            return res

        stack = []
        curr = node
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if curr.left is None and curr.right is None:
                res.append(curr.val)
            curr = curr.right
        return res
```

### recur

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        def dfs(node, lst):
            if node is None:
                return
            if node.left is None and node.right is None:
                lst.append(node.val)
            dfs(node.left, lst)
            dfs(node.right, lst)
        
        lst1 = []
        dfs(root1, lst1)
        lst2 = []
        dfs(root2, lst2)
        return lst1 == lst2
```

## refs

* [lc](https://leetcode.com/problems/leaf-similar-trees/)
