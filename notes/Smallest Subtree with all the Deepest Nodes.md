---
favorited: true
tags: [2019/11/30]
title: Smallest Subtree with all the Deepest Nodes
created: '2019-11-30T05:34:06.332Z'
modified: '2019-11-30T05:39:37.750Z'
---

# Smallest Subtree with all the Deepest Nodes

Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in its subtree.

 

Example 1:

Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation:

![pic](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/01/sketch1.png)

We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.
 

Note:

The number of nodes in the tree will be between 1 and 500.
The values of each node are unique.

## Solution

### 2-passes

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        
        if root.left is None and root.right is None:
            return root
        
        def get_height(node):
            if node is None:
                return 0
            left = get_height(node.left)
            right = get_height(node.right)
            return max(left, right) + 1
        
        height = get_height(root)
        
        self.res = None
        
        def helper(node, h):
            if not node:
                return node
            if h == height:
                return node
            left = helper(node.left, h+1)
            right = helper(node.right, h+1)
            return node if left and right else left or right
        
        return helper(root, 1)
```

### one-pass

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def helper(node):
            if node is None:
                return None, 0
            
            left, dist1 = helper(node.left)
            right, dist2 = helper(node.right)
            
            if dist1 > dist2:
                return left, dist1 + 1
            
            if dist2 > dist1:
                return right, dist2 + 1
            
            return node, dist1 + 1
        
        return helper(root)[0]
            
            
```

## refs

* [lc](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/)
