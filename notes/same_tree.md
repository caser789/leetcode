---
tags: [2019/08/08, BFS, leetcode/100]
title: Same Tree
created: '2019-08-08T16:10:30.452Z'
modified: '2019-08-09T02:18:14.418Z'
---

# Same Tree

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

### Example 1:

```
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
```

### Example 2:

```
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
```

### Example 3:

```

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
```


## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def isSameTree(self, a, b):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not a and not b:
            return True
        if not a:
            return False
        if not b:
            return False
        q = deque()
        q.append(a)
        q.append(b)
        while q:
            for i in range(len(q)/2):
                a = q.popleft()
                b = q.popleft()
                if a.val != b.val:
                    return False

                if a.left and b.left:
                    q.append(a.left)
                    q.append(b.left)
                elif a.left is None and b.left is None:
                    pass
                elif a.left is None:
                    return False
                else:
                    return False

                if a.right and b.right:
                    q.append(a.right)
                    q.append(b.right)
                elif a.right is None and b.right is None:
                    pass
                elif a.right is None:
                    return False
                else:
                    return False
        return True
```
