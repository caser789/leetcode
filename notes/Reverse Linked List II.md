---
tags: [2019/11/18, application/reverse, data structure/linked-list, leetcode/92]
title: Reverse Linked List II
created: '2019-11-18T05:15:53.272Z'
modified: '2019-11-26T07:00:22.559Z'
---

# Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

## Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return
        if head.next is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        h = dummy
        for i in range(m-1):
            h = h.next
        
        b = h.next
        h.next = None
        
        for i in range(n-m+1):
            nxt = b.next
            b.next = h.next
            h.next = b
            b = nxt
            
        while h.next:
            h = h.next
        h.next = b
        
        return dummy.next
                 
```

### better

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        h = head
        
        for _ in range(m-1):
            h = h.next
            prev = prev.next
            
        prev.next = None
        tail = h
        
        for _ in range(n-m+1):
            nxt = h.next
            h.next = prev.next
            prev.next = h
            h = nxt
            
        tail.next = h
        
        return dummy.next
        
        
```

## refs

* [lc](https://leetcode.com/problems/reverse-linked-list-ii/)

