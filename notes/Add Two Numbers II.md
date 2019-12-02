---
tags: [2019/11/26, application/add, application/reverse, data structure/linked-list, leetcode/445]
title: Add Two Numbers II
created: '2019-11-26T05:31:30.170Z'
modified: '2019-11-26T05:44:46.638Z'
---

# Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

## Solution

### reverse

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
        if not l1: return l2
        if not l2: return l1
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        l3 = add(l1, l2)
        return reverse(l3)
    

def reverse(head):
    d = ListNode(0)
    while head:
        nxt = head.next
        head.next = d.next
        d.next = head
        head = nxt
    return d.next

def _add(a, b, c):
    return divmod(a+b+c, 10)

def add(a, b):
    d = dummy = ListNode(0)
    c = 0
    while a and b:
        c, v = _add(a.val, b.val, c)
        d.next = ListNode(v)
        d = d.next
        a = a.next
        b = b.next
    while a:
        c, v = _add(a.val, 0, c)
        d.next = ListNode(v)
        d = d.next
        a = a.next
    while b:
        c, v = _add(0, b.val, c)
        d.next = ListNode(v)
        d = d.next
        b = b.next
    if c:
        d.next = ListNode(c)
    return dummy.next
        
```

### stack

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
        if not l1: return l2
        if not l2: return l1
        
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1)
            l1 = l1.next
        while l2:
            stack2.append(l2)
            l2 = l2.next
        
        dummy = ListNode(0)
        c = 0
        while stack1 and stack2:
            a = stack1.pop()
            b = stack2.pop()
            c, v = add(a.val, b.val, c)
            node = ListNode(v)
            node.next = dummy.next
            dummy.next = node
        while stack1:
            a = stack1.pop()
            b = 0
            c, v = add(a.val, 0, c)
            node = ListNode(v)
            node.next = dummy.next
            dummy.next = node
        while stack2:
            a = 0
            b = stack2.pop()
            c, v = add(0, b.val, c)
            node = ListNode(v)
            node.next = dummy.next
            dummy.next = node
        if c:
            node = ListNode(c)
            node.next = dummy.next
            dummy.next = node
        return dummy.next
            
            

def add(a, b, c):
    return divmod(a+b+c, 10)
```

## refs

* [lc](https://leetcode.com/problems/add-two-numbers-ii/)

