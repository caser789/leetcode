---
tags: [2019/11/28, data structure/queue, data structure/tree, leetcode/116, method/traversal/level/pointer]
title: Populating Next Right Pointers in Each Node
created: '2019-11-28T06:40:49.345Z'
modified: '2019-12-02T15:07:10.433Z'
---

# Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The '#' from the output is a sentinel which signifies the end of each level.
 

Constraints:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.

## Solution

### bfs

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
        
        q = [root]
        while q:
            nxt = []
            n = len(q)
            for i in range(n):
                if i + 1 < n:
                    q[i].next = q[i+1]
                else:
                    q[i].next = None
                
                if q[i].left:
                    nxt.append(q[i].left)
                if q[i].right:
                    nxt.append(q[i].right)
            q = nxt
        
        return root
```

### 2 pointers bfs

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

        head = root
        while head.left:
            cur = head
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next

            head = head.left
        return root

```

## refs 

* [lc](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)
