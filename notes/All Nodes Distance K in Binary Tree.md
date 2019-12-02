---
tags: [2020/01/01, data structure/graph, data structure/tree, leetcode/863, method/traversal/bfs, method/traversal/dfs/parent]
title: All Nodes Distance K in Binary Tree
created: '2019-12-01T08:34:26.605Z'
modified: '2019-12-01T08:38:36.016Z'
---

# All Nodes Distance K in Binary Tree

We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

![pic](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png)

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        
        def dfs(node, par=None):
            if node is None:
                return
            node.par = par
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root)
        
        queue = deque([(target, 0)])
        seen = {target}
        
        while queue:
            if queue[0][1] == K:
                return [node.val for node, d in queue]
            
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d+1))
        return []
            
```

## refs

* [lc](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)
