---
tags: [2019/11/30, data structure/heap, data structure/tree-in-array, data structure/tree/complete, design, leetcode/919]
title: Complete Binary Tree Inserter
created: '2019-11-30T06:29:18.714Z'
modified: '2019-12-07T08:12:08.992Z'
---

# Complete Binary Tree Inserter

A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following operations:

CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains complete, and returns the value of the parent of the inserted TreeNode;
CBTInserter.get_root() will return the head node of the tree.
 

Example 1:

Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]
Example 2:

Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]
 

Note:

The initial given tree is complete and contains between 1 and 1000 nodes.
CBTInserter.insert is called at most 10000 times per test case.
Every value of a given or inserted node is between 0 and 5000.


## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.deque = deque()
        self.root = root
        q = deque([root])
        
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = self.deque[0]
        self.deque.append(TreeNode(v))
        if not node.left:
            node.left = self.deque[-1]
        else:
            node.right = self.deque[-1]
            self.deque.popleft()
        return node.val
        

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
```

### dfs

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = [root]
        for node in self.nodes:
            if node.left:
                self.nodes.append(node.left)
            if node.right:
                self.nodes.append(node.right)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        n = len(self.nodes)
        self.nodes.append(TreeNode(v))
        if n % 2:
            self.nodes[(n-1)/2].left = self.nodes[n]
        else:
            self.nodes[(n-1)/2].right = self.nodes[n]
        return self.nodes[(n-1)/2].val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.nodes[0]



# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()

```

### heap 

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = [None]
        self.nodes.append(root)

        for node in self.nodes:
            if node is None: continue
            if node.left:
                self.nodes.append(node.left)

            if node.right:
                self.nodes.append(node.right)  
        
    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = TreeNode(v)
        self.nodes.append(node)
        n = len(self.nodes)
        index = n - 1
        p = index / 2
        if index % 2 == 0:
            self.nodes[p].left = node
        else:
            self.nodes[p].right = node
        
        return self.nodes[p].val
        
    def get_root(self):
        """
        :rtype: TreeNode
        """
        if len(self.nodes) > 1:
            return self.nodes[1]
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
```

## refs

* [lc](https://leetcode.com/problems/complete-binary-tree-inserter/)
