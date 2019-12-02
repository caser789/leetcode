---
deleted: true
tags: [2019/08/11, data structure/tree, leetcode/173, method/traversal/inorder]
title: Binary Search Tree Iterator
created: '2019-08-11T13:42:32.243Z'
modified: '2019-12-01T11:29:31.910Z'
---

# Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Example:
![pic](https://assets.leetcode.com/uploads/2018/12/25/bst-tree.png)


```
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
```

> next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
> You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        curr = root
        stack = []
        self.res = []
        self.i = 0
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            self.res.append(curr.val)
            curr = curr.right

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        i = self.res[self.i]
        self.i += 1
        return i

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.i < len(self.res)
```
