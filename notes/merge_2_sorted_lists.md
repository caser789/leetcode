---
tags: [2019/08/13, data structure/linked-list, leetcode/21, method/recursion, method/sort/merge]
title: Merge Two Sorted Lists
created: '2019-08-13T15:33:50.951Z'
modified: '2019-11-26T10:55:57.008Z'
---

# Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

### Example:

```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

## Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1:
            return l2

        if not l2:
            return l1

        if l1.val < l2.val:
            node = self.mergeTwoLists(l1.next, l2)
            l1.next = node
            return l1

        node = self.mergeTwoLists(l1, l2.next)
        l2.next = node
        return l2
```

### iter

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        
        d = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                nxt = l1.next
                l1.next = None
                d.next = l1
                d = d.next
                l1 = nxt
            else:
                nxt = l2.next
                l2.next = None
                d.next = l2
                d = d.next
                l2 = nxt
        if l1:
            d.next = l1
        if l2:
            d.next = l2
        return dummy.next
```

## refs

* [lc](https://leetcode.com/problems/merge-two-sorted-lists/)

