---
tags: [2019/11/29, data structure/tree, leetcode/662, method/recursion, method/traversal/bfs, method/traversal/dfs]
title: Maximum Width of Binary Tree
created: '2019-11-29T13:18:45.808Z'
modified: '2019-11-29T13:29:31.027Z'
---

# Maximum Width of Binary Tree

Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:

Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


Note: Answer will in the range of 32-bit signed integer.

## Solution


### bfs

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = [(root, 0, 0)]
        cur_depth = left = ans = 0
        
        for node, depth, pos in q:
            if not node: continue
            
            q.append((node.left, depth+1, pos*2))
            q.append((node.right, depth+1, pos*2+1))
            
            if cur_depth != depth:
                cur_depth = depth
                left = pos
            
            ans = max(pos-left+1, ans)
        
        return ans
```

### dfs

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.res = 0
        left = {}
        
        def dfs(node, depth=0, pos=0):
            if not node: return
            left.setdefault(depth, pos)
            self.res = max(self.res, pos-left[depth]+1)
            dfs(node.left, depth+1, pos*2)
            dfs(node.right, depth+1, pos*2+1)
        
        dfs(root)
        return self.res
```

## refs

* [lc](https://leetcode.com/problems/maximum-width-of-binary-tree/)
