---
tags: [2019/11/30, data structure/tree, leetcode/1026, method/recursion]
title: Maximum Difference Between Node and Ancestor
created: '2019-11-30T14:57:50.408Z'
modified: '2019-11-30T14:58:57.683Z'
---

# Maximum Difference Between Node and Ancestor

Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

 

Example 1:

![pic](https://assets.leetcode.com/uploads/2019/09/09/2whqcep.jpg)

Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
 

Note:

The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return
        
        def helper(node, mx, mn):
            if node is None:
                return mx-mn
            
            mx = max(mx, node.val)
            mn = min(mn, node.val)
            
            left = helper(node.left, mx, mn)
            right = helper(node.right, mx, mn)
            return max(left, right)
        
        
        return helper(root, root.val, root.val)
```

## refs

* [lc](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/)
