---
tags: [2019/11/03, application/add, data structure/linked-list, leetcode/2]
title: Add Two Numbers
created: '2019-11-01T23:53:11.551Z'
modified: '2019-11-26T05:12:31.199Z'
---

# Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

## Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        h1 = l1
        h2 = l2
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        c = 0
        d = dummy = ListNode(None)
        while h1 and h2:
            s = h1.val + h2.val + c
            c, s = divmod(s, 10)
            node = ListNode(s)
            d.next = node
            
            d = node
            h1 = h1.next
            h2 = h2.next
        
        while h1:
            s = h1.val + c
            c, s = divmod(s, 10)
            node = ListNode(s)
            d.next = node
            h1 = h1.next
            d = node
        
        while h2:
            s = h2.val + c
            c, s = divmod(s, 10)
            node = ListNode(s)
            d.next = node
            d = node
            h2 = h2.next
        
        if c:
            node = ListNode(c)
            d.next = node
        
        return dummy.next
            
```

## Schedule

* [x] 2019/11/02
* [ ] 2019/11/03
