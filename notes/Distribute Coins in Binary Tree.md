---
tags: [2019/11/30, data structure/tree, leetcode/979, method/recursion]
title: Distribute Coins in Binary Tree
created: '2019-11-30T11:19:42.602Z'
modified: '2019-11-30T11:21:26.082Z'
---

# Distribute Coins in Binary Tree

Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

 

Example 1:

![pic](https://assets.leetcode.com/uploads/2019/01/18/tree1.png)

Input: [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:

![pic](https://assets.leetcode.com/uploads/2019/01/18/tree2.png)

Input: [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.
Example 3:

![pic](https://assets.leetcode.com/uploads/2019/01/18/tree3.png)

Input: [1,0,2]
Output: 2
Example 4:



Input: [1,0,0,null,3]
Output: 4

![pic](https://assets.leetcode.com/uploads/2019/01/18/tree4.png)

Note:

1<= N <= 100
0 <= node.val <= N

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def count_available_coins(node):
            if node is None:
                return 0
            
            left = count_available_coins(node.left)
            right = count_available_coins(node.right)
            
            self.res += abs(left) + abs(right)
            return node.val - 1 + left + right
        
        count_available_coins(root)
        return self.res
```

## refs

* [lc](https://leetcode.com/problems/distribute-coins-in-binary-tree/)
