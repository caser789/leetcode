---
favorited: true
tags: [2019/11/29, data structure/tree, leetcode/655, method/recursion]
title: Print Binary Tree
created: '2019-11-29T13:03:02.827Z'
modified: '2019-11-29T13:04:38.738Z'
---

# Print Binary Tree

Print a binary tree in an m*n 2D string array following these rules:

The row number m should be equal to the height of the given binary tree.
The column number n should always be an odd number.
The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
Each unused space should contain an empty string "".
Print the subtrees following the same rules.
Example 1:
Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]
Example 2:
Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
Example 3:
Input:
      1
     / \
    2   5
   / 
  3 
 / 
4 
Output:

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
Note: The height of binary tree is in the range of [1, 10].

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        
        def get_height(node):
            if node is None:
                return 0
            left = get_height(node.left)
            right = get_height(node.right)
            return 1 + max(left, right)
        
        def fill(matrix, node, lo, hi, level):
            if node is None:
                return
            
            mi = (lo+hi) / 2
            matrix[level-1][mi] = str(node.val)
            
            fill(matrix, node.left, lo, mi-1, level+1)
            fill(matrix, node.right, mi+1, hi, level+1)
            
            
        
        height = get_height(root)
        
        array = [[''] * (2**height-1) for _ in range(height)]
        
        fill(array, root, 0, 2**height-2, 1)
        
        return array
```

## refs

* [lc](https://leetcode.com/problems/print-binary-tree/)
