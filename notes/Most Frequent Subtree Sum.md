---
tags: [2019/11/29, application/tree/subtree, data structure/tree, leetcode/508]
title: Most Frequent Subtree Sum
created: '2019-11-29T03:17:28.651Z'
modified: '2019-12-01T11:16:35.838Z'
---

# Most Frequent Subtree Sum

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        node_to_sum = {}
        
        def helper(node):
            if node is None:
                return 0
            
            x = helper(node.left)
            y = helper(node.right)
            s = x + y + node.val
            
            node_to_sum[node] = s
            return node_to_sum[node]
        
        helper(root)
        
        mfc = 0
        
        counter = {}
        for v in node_to_sum.values():
            counter.setdefault(v, 0)
            counter[v] += 1
            if counter[v] > mfc:
                mfc = counter[v]
        
        return [k for k, v in counter.items() if v == mfc]         
```

## refs

* [lc](https://leetcode.com/problems/most-frequent-subtree-sum/)
