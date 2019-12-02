---
tags: [2019/11/30, data structure/bst, data structure/monoqueue, data structure/tree, leetcode/1008, method/recursion, method/traversal/preorder]
title: Construct Binary Search Tree from Preorder Traversal
created: '2019-11-30T14:42:02.984Z'
modified: '2019-11-30T14:43:21.573Z'
---

# Construct Binary Search Tree from Preorder Traversal

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

 

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

![pic](https://assets.leetcode.com/uploads/2019/03/06/1266.png)

Note: 

1 <= preorder.length <= 100
The values of preorder are distinct.
Accepted

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        kv = {}
        stack = []
        n = len(preorder)
        for i in range(n):
            while stack and preorder[stack[-1]] < preorder[i]:
                j = stack.pop()
                kv[preorder[j]] = i
            
            stack.append(i)
        
        def helper(x, y):
            if y < x:
                return None
            
            v = preorder[x]
            if y == x:
                return TreeNode(v)
            i = kv.get(v, n)
            node = TreeNode(preorder[x])
            node.left = helper(x+1, i-1)
            node.right = helper(i, y)
            return node
        
        return helper(0, n-1)
```

## refs

* [lc](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)
