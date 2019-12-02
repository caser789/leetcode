---
tags: [2019/11/10, application/dedup, data structure/linked-list, leetcode/83, method/prev]
title: Remove Duplicates from Sorted List
created: '2019-09-07T09:11:50.715Z'
modified: '2019-11-26T12:29:55.907Z'
---

# Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

### Example 1:

Input: 1->1->2
Output: 1->2

### Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

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
        Input: 1->1->2->3->3
        Output: 1->2->3
        """
        if not head or not head.next:
            return head

        prev = head
        h = head.next

        while h:
            if h.val == prev.val:
                prev.next = h.next
                h = h.next
            else:
                prev = h
                h = h.next
        return head
```

### without dummy

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
        if head is None:
            return
        if head.next is None:
            return head
        
        h = head
        while h:
            while h.next and h.next.val == h.val:
                h.next = h.next.next
            h = h.next
        return head
```


## schedule

* [x] 0 2019/09/14
* [x] 1 2019/09/15
* [x] 1 2019/09/18
* [x] 1 2019/09/25
* [x] 1 2019/10/10
* [ ] 1 2019/11/10
