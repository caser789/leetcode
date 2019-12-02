---
tags: [2019/11/03, data structure/stack, data structure/tree, leetcode/114, method/recursion, method/traversal/dfs]
title: Flatten Binary Tree to Linked List
created: '2019-11-02T04:29:45.888Z'
modified: '2019-11-28T06:33:47.459Z'
---

# Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

```
    1
   / \
  2   5
 / \   \
3   4   6
```

The flattened tree should look like:

```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
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
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        
        stack = [root]
        h = dummy = TreeNode(None)
        
        while stack:
            n = stack.pop()
            
            if n.right:
                stack.append(n.right)
            
            if n.left:
                stack.append(n.left)
            
            n.left = None
            n.right = None
            h.right = n
            h = n
            
        return dummy.right
            
        
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
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        
        
        def helper(node):
            if node is None:
                return
            
            left = node.left
            right = node.right
            node.left = None
            node.right = None
            
            left = helper(left)
            right = helper(right)
            
            h = node
            if left:
                h.right = left
                
            while h.right:
                h = h.right
                
            h.right = right
            return node
            
        
        helper(root)
```

## schedule

* [x] 2019/11/02
* [ ] 2019/11/03

## refs

* [lc](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)
