---
tags: [2019/08/07, application/tree/compare, data structure/queue, data structure/stack, data structure/tree, leetcode/101, method/recursion, method/recursion/double, method/traversal/bfs, method/traversal/dfs]
title: Symmetric Tree
created: '2019-08-07T14:22:53.723Z'
modified: '2019-12-07T10:17:19.623Z'
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

### bfs

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
        if root is None:
            return True
        
        q = [root]
        
        while q:
            nxt = []
            n = len(q)
            i = 0
            j = n -1 
            while i <= j:
                a = q[i]
                b = q[j]
                
                if a.val != b.val: return False
                
                if a.left:
                    if not b.right: return False
                else:
                    if b.right: return False
                
                if a.right:
                    if not b.left: return False
                else:
                    if b.left: return False

                i += 1
                j -= 1
            
            for e in q:
                if e.left:
                    nxt.append(e.left)
                if e.right:
                    nxt.append(e.right)
            q = nxt
        return True
```

### dfs + stack

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
        stack = [root, root]
        while stack:
            a = stack.pop()
            b = stack.pop()
            if a is None and b is None: continue
            if a is None or b is None: return False
            if a.val != b.val: return False
            stack.append(a.left)
            stack.append(b.right)
            stack.append(a.right)
            stack.append(b.left)
        
        return True
```

### recursion

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
        def is_mirror(a, b):
            if a is None and b is None: return True
            if a is None or b is None: return False
            if a.val != b.val: return False
            if not is_mirror(a.left, b.right): return False
            if not is_mirror(a.right, b.left): return False
            return True
        
        return is_mirror(root, root)
```

## refs

* [lc](https://leetcode.com/problems/symmetric-tree/)
