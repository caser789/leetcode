---
tags: [2019/11/30, data structure/tree, leetcode/814, method/recursion]
title: Binary Tree Pruning
created: '2019-11-30T04:02:06.058Z'
modified: '2019-12-03T01:31:41.941Z'
---

# Binary Tree Pruning

We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

Example 1:
![pic](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png)
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]
 
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.


Example 2:
![pic](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png)
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]



Example 3:
![pic](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png)
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]



Note:

The binary tree will have at most 100 nodes.
The value of each node will only be 0 or 1.

## Solution

### recursion

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
        
        def helper(node):
            if node is None:
                return True
            
            left = helper(node.left)
            if left:
                node.left = None
            right = helper(node.right)
            if right:
                node.right = None
            
            
            valid = node.val == 0
            if valid and left and right:
                return True
            return False
        
        helper(root)
        return root
```

## refs

* [lc](https://leetcode.com/problems/binary-tree-pruning/)
