---
tags: [2019/11/14]
title: Binary Tree Pruning
created: '2019-11-14T01:39:59.729Z'
modified: '2019-11-14T01:41:26.268Z'
---

# Binary Tree Pruning

We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]
 
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.

![pic](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png)

Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]

![pic](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png)

Example 3:
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]

![pic](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png)

Note:

The binary tree will have at most 100 nodes.
The value of each node will only be 0 or 1.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        
        if root.left is None and root.right is None:
            if root.val == 1:
                return root
            return None
        
        if root.val == 1:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
            return root
        
        left = self.pruneTree(root.left)
        right = self.pruneTree(root.right)
        if not left and not right:
            return None
        root.left = left
        root.right = right
        return root
        
```

## refs

* [lc](https://leetcode.com/problems/binary-tree-pruning/)

