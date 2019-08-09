---
tags: [2019/08/09, data structure/tree, leetcode/145, method/traversal/postorder]
title: Binary Tree Postorder Traversal
created: '2019-08-09T08:53:54.674Z'
modified: '2019-08-09T08:59:21.014Z'
---

# Binary Tree Postorder Traversal

Given a binary tree, return the postorder traversal of its nodes' values.

### Example:

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res

        stack = []
        node = root
        last = None
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or node.right == last:
                    last = stack.pop()
                    res.append(last.val)
                    node = None
                else:
                    node = node.right
        return res
```

### method 2

```python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        node = root
        queue = deque()
        while node or stack:
            if node:
                stack.append(node)
                queue.appendleft(node.val)
                node = node.right
            else:
                node = stack.pop()
                node = node.left
        return list(queue)


_1 = TreeNode(1)
_2 = TreeNode(2)
_3 = TreeNode(3)
_4 = TreeNode(4)
_5 = TreeNode(5)
_6 = TreeNode(6)
_7 = TreeNode(7)
_1.left = _2
_1.right = _3
_2.left = _4
_2.right = _5
_4.left = _6
_4.right = _7

print Solution().postorderTraversal(_1)
```
