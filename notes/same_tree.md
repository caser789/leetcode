---
tags: [2019/08/08, application/tree/compare, application/tree/serialization, data structure/queue, data structure/stack, data structure/tree, leetcode/100, method/recursion, method/traversal/bfs, method/traversal/dfs]
title: Same Tree
created: '2019-08-08T16:10:30.452Z'
modified: '2019-12-01T12:00:42.399Z'
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

### stack

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None: return True
        if p is None: return False
        if q is None: return False
        stack = [p, q]
        while stack:
            a = stack.pop()
            if not stack:
                return False
            b = stack.pop()
            
            if a.val != b.val: return False
            
            if a.left:
                if not b.left: return False
                stack.append(a.left)
                stack.append(b.left)
            else:
                if b.left: return False
            
            if a.right:
                if not b.right: return False
                stack.append(a.right)
                stack.append(b.right)
            else:
                if b.right: return False
        
        return True
            
```

### recur

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        
        if p is None:
            return False
        
        if q is None:
            return False
        
        if p.val != q.val:
            return False
        
        if not self.isSameTree(p.left, q.left):
            return False
        
        if not self.isSameTree(p.right, q.right):
            return False
        
        return True
```

## refs

* [lc](https://leetcode.com/problems/same-tree/)
