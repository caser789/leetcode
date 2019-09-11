---
tags: [2019/09/18, leetcode/637, method/backtracking, method/traversal/bfs]
title: Average of Levels in Binary Tree
created: '2019-08-31T09:53:06.738Z'
modified: '2019-09-11T05:53:45.972Z'
---

# Average of Levels in Binary Tree


Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

### Example 1:

```
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
```

Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

## Note:

The range of node's value is in the range of 32-bit signed integer.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        count = []
        res = []
        average(root, 0, res, count)
        for level in range(len(res)):
            res[level] = res[level] / count[level]
        return res


def average(node, level, res, count):
    if node is None:
        return

    if level < len(res):
        res[level] += node.val
        count[level] += 1
    else:
        res.append(1.0*node.val)
        count.append(1)

    average(node.left, level+1, res, count)
    average(node.right, level+1, res, count)
```

## schedule

* [x] 0 2019/09/07
* [x] 1 2019/09/08
* [x] 1 2019/09/11
* [ ] 1 2019/09/18
