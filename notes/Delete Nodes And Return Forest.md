---
tags: [2019/11/30, data structure/tree, leetcode/1110, method/recursion, method/traversal/dfs]
title: Delete Nodes And Return Forest
created: '2019-11-30T15:44:42.437Z'
modified: '2019-12-08T10:58:25.545Z'
---

# Delete Nodes And Return Forest

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

 

Example 1:

![pic](https://assets.leetcode.com/uploads/2019/07/01/screen-shot-2019-07-01-at-53836-pm.png)

Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.

## Solution

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        
        to_delete = set(to_delete)
        res = []
        
        def helper(node, is_root=False):
            if node is None:
                return
            valid = node.val in to_delete
            if is_root and not valid:
                res.append(node)
            
            node.left = helper(node.left, valid)
            node.right = helper(node.right, valid)
            return None if valid else node
        
        helper(root, is_root=True)
        
        return res
        

```

## refs

* [lc](https://leetcode.com/problems/delete-nodes-and-return-forest/)
