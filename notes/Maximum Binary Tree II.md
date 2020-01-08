---
tags: [2019/11/30, application/tree/maximum, data structure/tree, leetcode/998, method/recursion]
title: Maximum Binary Tree II
created: '2019-11-30T14:29:10.958Z'
modified: '2019-12-08T10:55:21.362Z'
---

# Maximum Binary Tree II

We are given the root node of a maximum tree: a tree where every node has a value greater than any other value in its subtree.

Just as in the previous problem, the given tree was constructed from an list A (root = Construct(A)) recursively with the following Construct(A) routine:

If A is empty, return null.
Otherwise, let A[i] be the largest element of A.  Create a root node with value A[i].
The left child of root will be Construct([A[0], A[1], ..., A[i-1]])
The right child of root will be Construct([A[i+1], A[i+2], ..., A[A.length - 1]])
Return root.
Note that we were not given A directly, only a root node root = Construct(A).

Suppose B is a copy of A with the value val appended to it.  It is guaranteed that B has unique values.

Return Construct(B).

 

Example 1:

![pic](https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-1-2.png)

Input: root = [4,1,3,null,null,2], val = 5
Output: [5,4,null,1,3,null,null,2]
Explanation: A = [1,4,2,3], B = [1,4,2,3,5]
Example 2:

![pic](https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-2-2.png)

Input: root = [5,2,4,null,1], val = 3
Output: [5,2,4,null,1,null,3]
Explanation: A = [2,1,5,4], B = [2,1,5,4,3]
Example 3:

![pic](https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-3-2.png)

Input: root = [5,2,3,null,1], val = 4
Output: [5,2,4,null,1,3]
Explanation: A = [2,1,5,3], B = [2,1,5,3,4]
 

Note:

1 <= B.length <= 100

## Solution

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        if root is None:
            return TreeNode(val)
        
        if val > root.val:
            n = TreeNode(val)
            n.left = root
            return n
        
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
```

## refs

* [lc](https://leetcode.com/problems/maximum-binary-tree-ii/)
