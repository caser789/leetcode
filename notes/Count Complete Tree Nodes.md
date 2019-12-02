---
tags: [2019/11/28, data structure/tree, leetcode/222, method/recursion]
title: Count Complete Tree Nodes
created: '2019-11-28T10:18:06.750Z'
modified: '2019-11-28T10:25:31.271Z'
---

# Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        cnt = 0
        stack = [root]
        while stack:
            n = stack.pop()
            cnt += 1
            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)
        return cnt
```

### complete bst

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        left_depth = get_depth(root.left)
        right_depth = get_depth(root.right)
        if left_depth == right_depth:
            return pow(2, left_depth) + self.countNodes(root.right)
        return pow(2, right_depth) + self.countNodes(root.left)
    
    
def get_depth(node):
    if not node:
        return 0
    return 1 + get_depth(node.left)
```

## refs

* [lc](https://leetcode.com/problems/count-complete-tree-nodes/)
