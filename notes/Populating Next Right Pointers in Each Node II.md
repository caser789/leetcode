---
tags: [2019/11/28, data structure/tree, leetcode/117, method/traversal/bfs/pointer, method/traversal/level, TODO]
title: Populating Next Right Pointers in Each Node II
created: '2019-11-28T08:10:35.667Z'
modified: '2019-12-01T12:04:20.086Z'
---

# Populating Next Right Pointers in Each Node II

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 

Example 1:



Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 
 ![pic](https://assets.leetcode.com/uploads/2019/02/15/117_sample.png)

Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100


## Solution

```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        if root is None:
            return
        
        cur = root
        head = None
        prev = None
        
        while cur:
            
            while cur:
                
                if cur.left:
                    if prev:
                        prev.next = cur.left
                    else:
                        head = cur.left
                    prev = cur.left
                
                if cur.right:
                    if prev:
                        prev.next = cur.right
                    else:
                        head = cur.right
                    prev = cur.right
                
                cur = cur.next
            
            cur = head
            head = None
            prev = None
            
        return root
```

## refs

* [lc](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)
