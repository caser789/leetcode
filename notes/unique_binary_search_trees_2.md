---
tags: [2019/08/13, application/combination, data structure/bst, data structure/tree, leetcode/95, method/recursion]
title: Unique Binary Search Trees II
created: '2019-08-13T15:38:16.731Z'
modified: '2019-12-01T11:57:03.139Z'
---

# Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

### Example:

```
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return generate(range(1, n+1))
              

def generate(nums):
    n = len(nums)
    if not n:
        return [None]
    if n == 1:
        return [TreeNode(nums[0])]
    if n == 2:
        a = TreeNode(nums[0])
        a.right = TreeNode(nums[1])
        
        b = TreeNode(nums[1])
        b.left = TreeNode(nums[0])
        return [a, b]
    
    res = []
    for i in range(n):
        v = nums[i]
        left = nums[:i]
        right = nums[i+1:]
        left_nodes = generate(left)
        right_nodes = generate(right)
        for a in left_nodes:
            for b in right_nodes:
                n = TreeNode(v)
                n.left = a
                n.right = b
                res.append(n)
    return res
```

## refs

* [lc](https://leetcode.com/problems/unique-binary-search-trees-ii/)

