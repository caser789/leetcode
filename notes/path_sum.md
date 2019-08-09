---
tags: [2019/08/08, leetcode/112]
title: Path Sum
created: '2019-08-09T02:19:18.029Z'
modified: '2019-08-09T02:19:48.307Z'
---

# Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

>  A leaf is a node with no children.

### Example:

```
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
```

## Solution

```python
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root and not sum:
            return False

        if not root and sum:
            return False

        nodes = deque()
        nodes.append(root)

        paths = deque()
        paths.append(0)

        while nodes:
            for _ in range(len(nodes)):
                node = nodes.popleft()
                path = paths.popleft()
                path += node.val

                if node.left:
                    nodes.append(node.left)
                    paths.append(path)

                if node.right:
                    nodes.append(node.right)
                    paths.append(path)

                if not node.left and not node.right:
                    if path == sum:
                        return True
        return False


_5 = TreeNode(5)
_4 = TreeNode(4)
_8 = TreeNode(8)
_11 = TreeNode(11)
_13 = TreeNode(13)
__4 = TreeNode(4)
_7 = TreeNode(7)
_2 = TreeNode(2)
_1 = TreeNode(1)

_5.left = _4
_5.right = _8
_4.left = _11
_11.left = _7
_11.right = _2
_8.left = _13
_8.right = __4
__4.right = _1


```
