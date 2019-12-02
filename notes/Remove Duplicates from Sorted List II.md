---
tags: [2019/11/18, application/dedup, data structure/linked-list, leetcode/82, method/prev]
title: Remove Duplicates from Sorted List II
created: '2019-11-18T05:32:12.248Z'
modified: '2019-11-26T12:29:48.740Z'
---

# Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

## Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Input: 1->2->3->3->4->4->5
        Output: 1->2->5

        Input: 1->1->1->2->3
        Output: 2->3

        """
        if head is None:
            return
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            if prev.next is cur:
                prev = prev.next
            else:
                prev.next = cur.next
            cur = cur.next
        return dummy.next

```

### brute force

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        d = dummy = ListNode(0)
        
        while head:
            if head.next and head.val == head.next.val:
                v = head.val
                while head and head.val == v:
                    head = head.next
                continue
                
            if head:
                nxt = head.next
                head.next = None
                
                d.next = head
                d = d.next
                
                head = nxt
        
        return dummy.next
        
```

## refs

* [lc](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

