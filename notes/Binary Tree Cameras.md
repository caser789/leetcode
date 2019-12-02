---
tags: [2019/11/30, data structure/tree, leetcode/968, method/dp, method/greedy, method/traversal/dfs/parent]
title: Binary Tree Cameras
created: '2019-11-30T09:36:59.257Z'
modified: '2019-11-30T09:47:18.418Z'
---

# Binary Tree Cameras

Given a binary tree, we install cameras on the nodes of the tree. 

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.

 

Example 1:

![pic](https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_01.png)

Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
Example 2:

![pic](https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_02.png)

Input: [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

Note:

The number of nodes in the given tree will be in the range [1, 1000].
Every node has value 0.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 0: not covered
        # 1: covered without camera
        # 2: covered with camera
        
        def solve(node):
            if node is None:
                return 0, 0, float('inf')
            
            left = solve(node.left)
            right = solve(node.right)
            
            dp0 = left[1] + right[1]
            dp1 = min(left[2] + min(right[1:]), right[2] + min(left[1:]))
            dp2 = min(left) + min(right) + 1
            
            return dp0, dp1, dp2
        
        return min(solve(root)[1:])
            
        
        
```

### greedy

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.res = 0
        covered = {None}
        
        def dfs(node, par=None):
            if node is None:
                return
            
            dfs(node.left, node)
            dfs(node.right, node)
            
            if (
                par is None and node not in covered or 
                node.left not in covered or 
                node.right not in covered
            ):
                self.res += 1
                covered.update({node, par, node.left, node.right})
        
        dfs(root)
        return self.res
```

## refs

* [lc](https://leetcode.com/problems/binary-tree-cameras/)
