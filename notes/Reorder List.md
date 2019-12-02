---
tags: [2019/11/26, data structure/linked-list, leetcode/143, method/reverse, method/sort/merge]
title: Reorder List
created: '2019-11-26T11:21:21.241Z'
modified: '2019-11-26T11:23:01.546Z'
---

# Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

## Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        f   f   f
        s s s
        1 2 3 4 5
        
        1 2 3 4
        f   f   f
        s s s
        """
        if head is None or head.next is None:
            return head
        
        fast = slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if prev:
                prev = prev.next
            else:
                prev = head
        
        prev.next = None
        
        slow = reverse(slow)
        
        a = head
        b = slow
        return merge(a, b)
        

def reverse(node):
    dummy = ListNode(0)
    while node:
        nxt = node.next
        node.next = dummy.next
        dummy.next = node
        node = nxt
    return dummy.next

def merge(a, b):
    d = dummy = ListNode(0)
    while a and b:
        aa = a.next
        bb = b.next
        d.next = a
        d = d.next
        d.next = b
        d = d.next
        a = aa
        b = bb
        
    if a:
        d.next = a
    if b:
        d.next = b
    return dummy.next
        

        
```

## refs

* [lc](https://leetcode.com/problems/reorder-list/)

