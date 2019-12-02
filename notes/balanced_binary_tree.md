---
tags: [2019/08/09, application/tree/depth, data structure/tree, leetcode/110, method/recursion]
title: Balanced Binary Tree
created: '2019-08-09T03:30:53.379Z'
modified: '2019-12-01T12:11:37.936Z'
---

# Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

### Example 1:

```
Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.
```

### Example 2:

```
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
```

## Solution

```python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        node = root
        last = None
        depths = {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or node.right == last:
                    last = stack.pop()
                    left = depths.get(last.left, 0)
                    right = depths.get(last.right, 0)
                    if abs(left - right) > 1:
                        return False
                    depths[last] = max(left, right) + 1
                    node = None
                else:
                    node = node.right
        return True



_1 = TreeNode(1)
_2 = TreeNode(2)
_3 = TreeNode(3)
_4 = TreeNode(4)
_5 = TreeNode(5)
_6 = TreeNode(6)
_7 = TreeNode(7)

_1.left = _2
_1.right = _3
_2.left = _4
_2.right = _5
_4.left = _6
_4.right = _7

Solution().isBalanced(_1)
```

### recursion

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        node_to_height = {None: 0}
        
        def height(node):
            if node is None:
                return 0
            if node in node_to_height:
                return node_to_height[node]
            x = height(node.left)
            y = height(node.right)
            node_to_height[node] = max(x, y) + 1
            return node_to_height[node]
        
        def is_balance(node):
            if node is None:
                return True
            if not is_balance(node.left):
                return False
            if not is_balance(node.right):
                return False
            x = height(node.left)
            y = height(node.right)
            return abs(x-y) < 2
            
        
        return is_balance(root)
```

## refs

* [lc](https://leetcode.com/problems/balanced-binary-tree/)
