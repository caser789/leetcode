---
tags: [2019/11/30, application/restore-tree, data structure/tree, leetcode/889, method/recursion]
title: Construct Binary Tree from Preorder and Postorder Traversal
created: '2019-11-30T05:14:26.700Z'
modified: '2019-11-30T05:15:45.873Z'
---

# Construct Binary Tree from Preorder and Postorder Traversal

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

 

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
 

Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        n = len(pre)
        
        v_to_i = {}
        for i, v in enumerate(post):
            v_to_i[v] = i
        
        def helper(i, j, x, y):
            if j < i:
                return None
            if i == j:
                return TreeNode(pre[i])
            
            v = pre[i+1]
            index = v_to_i[v]
            length = index - x + 1
            
            node = TreeNode(pre[i])
            node.left = helper(i+1, i+length, x, index)
            node.right = helper(i+length+1, j, index+1, y)
            return node
        
        
        return helper(0, n-1, 0, n-1)
```

## refs

* [lc](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)
