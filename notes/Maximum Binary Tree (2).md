---
favorited: true
tags: [2019/11/29, data structure/monoqueue, data structure/tree, leetcode/654, method/recursion]
title: Maximum Binary Tree
created: '2019-11-29T09:24:47.035Z'
modified: '2019-11-29T09:36:18.089Z'
---

# Maximum Binary Tree

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
Note:
The size of the given array will be in the range [1,1000].

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        i = 0
        v = nums[0]
        for j in range(1, len(nums)):
            if nums[j] > v:
                v = nums[j]
                i = j
        
        node = TreeNode(v)
        node.left = self.constructMaximumBinaryTree(nums[:i])
        node.right = self.constructMaximumBinaryTree(nums[i+1:])
        return node
```

### monoqueue

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return

        stack = [ ]
        last = None
        for num in nums:
            while stack and stack[-1].val < num:
                last = stack.pop()

            node = TreeNode(num)
            if stack:
                stack[-1].right = node

            if last:
                node.left = last
            stack.append(node)
            last = None

        return stack[0]

```

## refs

* [lc](https://leetcode.com/problems/maximum-binary-tree/)
* [dis](https://leetcode.com/problems/maximum-binary-tree/discuss/258364/Python-O(n)-solution-with-explanation.)
