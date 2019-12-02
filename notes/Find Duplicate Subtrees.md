---
tags: [2019/11/29, application/tree/serialization, application/tree/subtree, data structure/tree, leetcode/652, method/recursion]
title: Find Duplicate Subtrees
created: '2019-11-29T08:54:27.463Z'
modified: '2019-12-01T11:17:50.891Z'
---

# Find Duplicate Subtrees

Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.


## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if root is None:
            return []
        
        nodes = []
   
        count = {}
        
        def dump(node):
            if node is None:
                return '#'
            
            left = dump(node.left)
            right = dump(node.right)
            res = '# {} {} {}'.format(node.val, left, right)
         
            count.setdefault(res, 0)
            count[res] += 1
            if count[res] == 2:
                nodes.append(node)
            return res
        
        dump(root)
        return nodes    
```

### O(n)

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = []
        count = {}
        self.uid = 0
        node_to_uid = {}
        
        def lookup(node):
            if not node: return
            k = (node.val, lookup(node.left), lookup(node.right))
            
            if k not in node_to_uid:
                node_to_uid[k] = self.uid
                self.uid += 1
            
            uid = node_to_uid[k]
            count.setdefault(uid, 0)
            count[uid] += 1
            if count[uid] == 2:
                res.append(node)
            return uid
        
        lookup(root)
        return res
```

## refs

* [lc](https://leetcode.com/problems/find-duplicate-subtrees/)

