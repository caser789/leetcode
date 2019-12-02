---
tags: [2019/11/29, data structure/queue, data structure/stack, data structure/tree, leetcode/623, method/recursion, method/traversal/bfs, method/traversal/dfs]
title: Add One Row to Tree
created: '2019-11-29T08:13:38.503Z'
modified: '2019-11-29T08:36:05.886Z'
---

# Add One Row to Tree

Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:
Input: 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

v = 1

d = 2

Output: 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5   

Example 2:
Input: 
A binary tree as following:
      4
     /   
    2    
   / \   
  3   1    

v = 1

d = 3

Output: 
      4
     /   
    2
   / \    
  1   1
 /     \  
3       1
Note:
The given d is in range [1, maximum depth of the given tree + 1].
The given binary tree has at least one tree node.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            n = TreeNode(v)
            n.left = root
            return n
        
        def insert(node, depth):
            if node is None:
                return
            
            if depth == d - 1:
                left = node.left
                node.left = TreeNode(v)
                node.left.left = left
                
                right = node.right
                node.right = TreeNode(v)
                node.right.right = right
                
            else:
                insert(node.left, depth+1)
                insert(node.right, depth+1)
        
        insert(root, 1)
        return root
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
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            n = TreeNode(v)
            n.left = root
            return n
        
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if node is None: continue
            if depth > d - 1: continue
            if depth == d - 1:
                left = node.left
                node.left = TreeNode(v)
                node.left.left = left
                
                right = node.right
                node.right = TreeNode(v)
                node.right.right = right
            else:
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
        
        return root
```

### queue + bfs

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            n = TreeNode(v)
            n.left = root
            return n
        
        q = [root]
        for i in range(d-2):
            nxt = []
            for e in q:
                if e.left:
                    nxt.append(e.left)
                if e.right:
                    nxt.append(e.right)
            q = nxt
        
        for e in q:
            left = e.left
            e.left = TreeNode(v)
            e.left.left = left
            
            right = e.right
            e.right = TreeNode(v)
            e.right.right = right
        
        return root
```

## refs

* [lc](https://leetcode.com/problems/add-one-row-to-tree/)
