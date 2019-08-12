---
tags: [2019/08/12, leetcode/24, method/recursion]
title: Swap Nodes in Pairs
created: '2019-08-12T15:27:45.394Z'
modified: '2019-08-12T15:28:17.701Z'
---

# Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

### Example:

```
Given 1->2->3->4, you should return the list as 2->1->4->3.
```

## Solution

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
        if not head:
            return
        if not head.next:
            return head

        a = head
        b = head.next
        c = self.swapPairs(b.next)
        b.next = a
        a.next = c
        return b
```
