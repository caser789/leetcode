---
tags: [2019/08/13, leetcode/206, method/recursion]
title: Reverse Linked List
created: '2019-08-13T15:23:57.726Z'
modified: '2019-11-26T06:10:09.613Z'
---

# Reverse Linked List

Reverse a singly linked list.

### Example:

```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

> A linked list can be reversed either iteratively or recursively. Could you implement both?


## Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
```

### iter

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        while head:
            nxt = head.next
            head.next = dummy.next
            dummy.next = head
            head = nxt
        return dummy.next
```

## refs

* [lc](https://leetcode.com/problems/reverse-linked-list/submissions/)

