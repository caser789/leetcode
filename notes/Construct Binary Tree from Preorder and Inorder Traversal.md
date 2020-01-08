---
tags: [2019/11/09, application/tree/build, data structure/tree, leetcode/105, method/recursion]
title: Construct Binary Tree from Preorder and Inorder Traversal
created: '2019-11-09T04:58:51.607Z'
modified: '2019-12-03T01:36:14.349Z'
---

# Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

```
    3
   / \
  9  20
    /  \
   15   7
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """  
        if not preorder:
            return
        
        d = {n: i for i, n in enumerate(inorder)}
        
        def build(pi, pj, ii, ij):
            num = preorder[pi]
            n = TreeNode(num)
            if pi == pj:
                return n 
            
            i = d[num]
            len_left = i - ii
            len_right = ij - i
            if len_left:
                n.left = build(pi+1, pi+len_left, i-len_left, i-1)
            if len_right:
                n.right = build(pi+len_left+1, pi+len_left+len_right, i+1, i+len_right)
            return n
            
        n = len(preorder)
        return build(0, n-1, 0, n-1)
        
```

### better

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        n = len(preorder)
        v_to_i = {}
        for i, v in enumerate(inorder):
            v_to_i[v] = i
        
        def build(i, j, m, n):
            if j < i:
                return None
            
            v = preorder[i]
            k = v_to_i[v]
            
            length = k - m
            
            node = TreeNode(v)
            node.left = build(i+1, i+1+length-1 , m, k-1)
            node.right = build(i+1+length,j , k+1, n)
            return node
                   
        return build(0, n-1, 0, n-1)
```

## refs

* [lc](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

