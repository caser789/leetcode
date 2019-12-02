---
tags: [2019/11/18, data structure/linked-list, leetcode/109, method/2-pointers]
title: Convert Sorted List to Binary Search Tree
created: '2019-11-18T01:15:20.536Z'
modified: '2019-11-26T13:50:14.324Z'
---

# Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

## Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        f    f   f
             s
        10 3 0 5 9
        """
        if head is None:
            return
        
        if head.next is None:
            return TreeNode(head.val)
        
        slow = fast = head
        p = None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if p is None:
                p = head
            else:
                p = p.next
        
        p.next = None
        right_lst = slow.next
        slow.next = None
        
        left = self.sortedListToBST(head)
        right = self.sortedListToBST(right_lst)
        node = TreeNode(slow.val)
        node.left = left
        node.right = right
        return node
        
        
        
        
        
```

## refs

* [lc](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)

