---
tags: [2019/11/05, leetcode/437]
title: Path Sum III
created: '2019-09-07T06:54:48.784Z'
modified: '2019-10-07T05:12:22.824Z'
---

# Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

### Example:

```
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        a = count(root, sum)
        b = self.pathSum(root.left, sum)
        c = self.pathSum(root.right, sum)
        return a + b + c

def count(node, s):
    if node is None:
        return 0
    mid = 1 if node.val == s else 0
    left = count(node.left, s - node.val)
    right = count(node.right, s-node.val)
    return mid + left + right
```


## schedule

* [x] 0 2019/09/09
* [x] 1 2019/09/10
* [x] 1 2019/09/13
* [x] 1 2019/09/20
* [x] 1 2019/10/05
* [ ] 1 2019/11/05
