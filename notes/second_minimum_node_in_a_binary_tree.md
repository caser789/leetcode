---
tags: [2019/12/02, data structure/tree, leetcode/671, method/recursion]
title: Second Minimum Node In a Binary Tree
created: '2019-09-07T06:56:52.544Z'
modified: '2019-11-29T13:38:31.791Z'
---

# Second Minimum Node In a Binary Tree

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

### Example 1:

```
Input:
    2
   / \
  2   5
     / \
    5   7
```

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.


### Example 2:

```
Input:
    2
   / \
  2   2
```

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 99999999999999
        min1 = root.val

        def dfs(node):
            if node:
                if min1 < node.val < self.res:
                    self.res = node.val
                elif node.val == min1:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        return self.res if self.res < 99999999999999 else -1
```


## schedule

* [x] 0 2019/09/10
* [x] 1 2019/09/11
* [x] 1 2019/09/14
* [x] 1 2019/09/21
* [x] 1 2019/10/06
* [x] 1 2019/10/07
* [x] 1 2019/10/10
* [x] 1 2019/10/17
* [x] 1 2019/11/01
* [ ] 1 2019/12/02


## refs

* [lc](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/)
