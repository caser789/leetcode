---
tags: [2019/08/09, application/tree/path, data structure/stack, data structure/tree, leetcode/257, method/recursion, method/traversal/dfs]
title: Binary Tree Paths
created: '2019-08-09T04:06:28.553Z'
modified: '2019-12-02T14:40:03.171Z'
---

# Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

>  A leaf is a node with no children.

### Example:

```
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
```


## Solutions

```python
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        res = []
        stack = [(root, [])]
        while stack:
            node, lst = stack.pop()
            if not node.left and not node.right:
                lst.append(node.val)
                res.append('->'.join(str(e) for e in lst))

            if node.right:
                _lst = lst[:]
                _lst.append(node.val)
                stack.append((node.right, _lst))

            if node.left:
                _lst = lst[:]
                _lst.append(node.val)
                stack.append((node.left, _lst))
        return res


_1 = TreeNode(1)
_2 = TreeNode(2)
_3 = TreeNode(3)
_5 = TreeNode(5)
_1.left = _2
_1.right = _3
_2.right = _5

print Solution().binaryTreePaths(_1)
```

### recur

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        
        res = []
        
        tmp = [root.val]
        
        def helper(node):
            if node.left is None and node.right is None:
                res.append('->'.join(str(e) for e in tmp))
                return
            
            if node.left:
                tmp.append(node.left.val)
                helper(node.left)
                tmp.pop()
            
            if node.right:
                tmp.append(node.right.val)
                helper(node.right)
                tmp.pop()
        
        helper(root)
        return res
```

## refs

* [lc](https://leetcode.com/problems/binary-tree-paths/)

