---
tags: [2019/08/12, leetcode/24, method/recursion]
title: Swap Nodes in Pairs
created: '2019-08-12T15:27:45.394Z'
modified: '2019-11-26T10:04:06.785Z'
---

# Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

### Example:

```
Given 1->2->3->4, you should return the list as 2->1->4->3.
```

## Solution

### iter

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        p = None
        h = head.next
        while head and head.next:
            a, b, c = head, head.next, head.next.next
            
            a.next = None
            b.next = a
            if p is not None:
                p.next = b
            p = a
            
            head = c
        if head:
            p.next = head
        
        return h
```

### recur

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.next is None:
            return head
        
        a, b = head, head.next
        
        a.next = self.swapPairs(b.next)
        b.next = a
        return b
```

## refs

* [lc](https://leetcode.com/problems/swap-nodes-in-pairs/submissions/)

