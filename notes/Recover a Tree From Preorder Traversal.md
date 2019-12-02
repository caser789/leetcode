---
tags: [2019/12/01, data structure/tree, leetcode/1028, method/tree-from-stack]
title: Recover a Tree From Preorder Traversal
created: '2019-12-01T02:50:21.321Z'
modified: '2019-12-01T02:51:59.569Z'
---

# Recover a Tree From Preorder Traversal

We run a preorder depth first search on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  (If the depth of a node is D, the depth of its immediate child is D+1.  The depth of the root node is 0.)

If a node has only one child, that child is guaranteed to be the left child.

Given the output S of this traversal, recover the tree and return its root.

 

Example 1:

![pic](https://assets.leetcode.com/uploads/2019/04/08/recover-a-tree-from-preorder-traversal.png)

Input: "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
Example 2:

![pic](https://assets.leetcode.com/uploads/2019/04/11/screen-shot-2019-04-10-at-114101-pm.png)

Input: "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]
 

Example 3:

![pic](https://assets.leetcode.com/uploads/2019/04/11/screen-shot-2019-04-10-at-114955-pm.png)

Input: "1-401--349---90--88"
Output: [1,401,null,349,88,90]
 

Note:

The number of nodes in the original tree is between 1 and 1000.
Each node will have a value between 1 and 10^9.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        stack = []
        i = 0
        n = len(S)
        while i < n:
            level = 0
            val = ''
            while i < n and S[i] == '-':
                level += 1
                i += 1
            while i < n and S[i] != '-':
                val = val + S[i]
                i += 1
            while len(stack) > level:
                stack.pop()
            
            node = TreeNode(val)
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
```

## refs

* [lc](https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/)
