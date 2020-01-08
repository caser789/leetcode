---
tags: [2019/11/30, application/tree/path, data structure/tree, leetcode/988, method/recursion, method/traversal/dfs]
title: Smallest String Starting From Leaf
created: '2019-11-30T11:55:10.645Z'
modified: '2019-12-03T14:47:37.289Z'
---

# Smallest String Starting From Leaf

Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents 'b', and so on.

Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

(As a reminder, any shorter prefix of a string is lexicographically smaller: for example, "ab" is lexicographically smaller than "aba".  A leaf of a node is a node that has no children.)

 

Example 1:

![pic](https://assets.leetcode.com/uploads/2019/01/30/tree1.png)

Input: [0,1,2,3,4,3,4]
Output: "dba"
Example 2:

![pic](https://assets.leetcode.com/uploads/2019/01/30/tree2.png)

Input: [25,1,3,1,3,0,2]
Output: "adz"
Example 3:

![pic](https://assets.leetcode.com/uploads/2019/02/01/tree3.png)

Input: [2,2,1,null,1,0,null,0]
Output: "abc"
 

Note:

The number of nodes in the given tree will be between 1 and 8500.
Each node in the tree will have a value between 0 and 25.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        
        def node_to_chr(node):
            return chr(ord('a') + node.val)
            
        self.res = None
        tmp = [node_to_chr(root)]
        
        
        def find(node):
            if node is None:
                return
            
            if node.left is None and node.right is None:
                s = ''.join(tmp[::-1])
                if self.res is None or s < self.res:
                    self.res = s     
            
            if node.left:
                tmp.append(node_to_chr(node.left))
                find(node.left)
                tmp.pop()
            
            if node.right:
                tmp.append(node_to_chr(node.right))
                find(node.right)
                tmp.pop()
            
        
        find(root)
        return self.res
```

### short

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        
        tmp = []
        self.res = None
        
        def helper(node):          
            tmp.append(chr(ord('a')+node.val))
            if node.left is None and node.right is None:
                s = ''.join(tmp[::-1])
                if self.res is None or s < self.res:
                    self.res = s
            
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            
            tmp.pop()                
 
        helper(root)
        
        return self.res
```

## refs

* [lc](https://leetcode.com/problems/smallest-string-starting-from-leaf/)
