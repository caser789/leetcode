---
tags: [2019/09/13, leetcode/501, method/traversal/inorder]
title: Find Mode in Binary Search Tree
created: '2019-09-07T07:00:15.112Z'
modified: '2019-09-10T14:09:15.763Z'
---

# Find Mode in Binary Search Tree

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.


### For example:

Given BST [1,null,2,2],

```
   1
    \
     2
    /
   2
```


return [2].

### Note:
If a tree has more than one mode, you can return them in any order.

### Follow up:
Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).



## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        v = None
        cnt = 0
        max_cnt = 0

        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if v is None:
                v = node.val
                cnt = 1
            elif v == node.val:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
                v = node.val
            node = node.right
        max_cnt = max(max_cnt, cnt)

        res = []
        cnt = 0
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if v is None:
                v = node.val
                cnt = 1
            elif v == node.val:
                cnt += 1
            else:
                if cnt == max_cnt:
                    res.append(v)
                cnt = 1
                v = node.val
            node = node.right
        if cnt == max_cnt:
            res.append(v)
        return res

```


## schedule

* [x] 0 2019/09/09
* [x] 1 2019/09/10
* [ ] 1 2019/09/13

