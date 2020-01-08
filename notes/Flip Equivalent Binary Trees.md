---
tags: [2019/11/30, application/tree/compare, application/tree/flip, application/tree/serialization, data structure/tree, leetcode/951, method/recursion]
title: Flip Equivalent Binary Trees
created: '2019-11-30T07:07:40.135Z'
modified: '2019-12-04T14:21:35.020Z'
---

# Flip Equivalent Binary Trees

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes root1 and root2.

 

Example 1:

Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Flipped Trees Diagram
 

Note:

Each tree will have at most 100 nodes.
Each value in each tree will be a unique integer in the range [0, 99].

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        if root1 is root2:
            return True
        
        if root1 is None:
            return False
        if root2 is None:
            return False
        if root1.val != root2.val:
            return False
        
        # not self-fliped 
        x = self.flipEquiv(root1.left, root2.left)
        y = self.flipEquiv(root1.right, root2.right)
        
        if x and y:
            return True
        
        # self-fliped
        x = self.flipEquiv(root1.left, root2.right)
        y = self.flipEquiv(root1.right, root2.left)
        if x and y:
            return True
        return False
```

### serialization

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        def dfs(node, lst):
            if node is None:
                return
            lst.append(str(node.val))
            
            left = node.left.val if node.left else -1
            right = node.right.val if node.right else -1
            
            if left < right:
                dfs(node.left, lst)
                dfs(node.right, lst)
            else:
                dfs(node.right, lst)
                dfs(node.left, lst)
            
            lst.append('#')
            
        lst1 = []
        lst2 = []
        dfs(root1, lst1)
        dfs(root2, lst2)
        return lst1 == lst2
            
```

## refs

* [lc](https://leetcode.com/problems/flip-equivalent-binary-trees/)
