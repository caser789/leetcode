---
tags: [2019/11/28, data structure/tree, leetcode/337, method/dp/neighbour]
title: House Robber III
created: '2019-11-28T12:22:25.523Z'
modified: '2019-11-28T12:34:59.713Z'
---

# House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

## Solution

### brute force

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            if node is None:
                return 0
            
            val = 0
            if node.left:
                val += helper(node.left.left) + helper(node.left.right)
            if node.right:
                val += helper(node.right.left) + helper(node.right.right)
            return max(val+node.val, helper(node.left) + helper(node.right))
        
        return helper(root)
        
```

### top-down

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cache = {}
        def helper(node):
            if node is None:
                return 0
            if node in cache:
                return cache[node]
            val = 0
            if node.left:
                val += helper(node.left.left) + helper(node.left.right)
            if node.right:
                val += helper(node.right.left) + helper(node.right.right)
            res = max(val+node.val, helper(node.left) + helper(node.right))
            cache[node] = res
            return cache[node]
        
        return helper(root)
        
```

### neighbour dp

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def helper(node):
            if node is None:
                return 0, 0
            
            left = helper(node.left)
            right = helper(node.right)
            
            a = max(left[0], left[1]) + max(right[0], right[1])
            b = node.val + left[0] + right[0]
            
            return a, b
            
        
        a, b = helper(root)
        return max(a, b)
```

## refs

* [lc](https://leetcode.com/problems/house-robber-iii/)
* [dis](https://leetcode.com/problems/house-robber-iii/discuss/79330/Step-by-step-tackling-of-the-problem)

