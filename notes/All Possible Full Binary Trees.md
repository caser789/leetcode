---
favorited: true
tags: [2019/11/14, application/combination, data structure/tree, leetcode/894, method/dp]
title: All Possible Full Binary Trees
created: '2019-11-14T05:03:43.203Z'
modified: '2019-12-03T01:37:01.721Z'
---

# All Possible Full Binary Trees

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

![pic](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/22/fivetrees.png)
 

Example 1:

Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Explanation:

 

Note:

1 <= N <= 20

## Solution

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        f(1) = 1
        f(2) = 0
        f(3) = 1
        
        """

        kv = {}
        
        def find(n):
            if n % 2 == 0:
                return []
            if n == 1:
                nodes = [TreeNode(0)]
                kv[n] = nodes
                return kv[n]
            
            res = []
            for i in range(1, n):
                if i % 2 == 0: continue
                left = find(i)
                right = find(n-1-i)
                for x in left:
                    for y in right:
                        node = TreeNode(0)
                        node.left = x
                        node.right = y
                        res.append(node)
            kv[n] = res
            return kv[n]
                        
            
            
            
        return find(N)
            
            
```

## refs

* [lc](https://leetcode.com/problems/all-possible-full-binary-trees/)

