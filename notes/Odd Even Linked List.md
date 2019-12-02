---
tags: [2019/11/26, data structure/linked-list, leetcode/328, method/2-pointers]
title: Odd Even Linked List
created: '2019-11-26T14:57:43.745Z'
modified: '2019-11-26T14:58:35.482Z'
---

# Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...

## Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        a = aa = ListNode(0)
        b = bb = ListNode(0)
        
        while head and head.next:
            x = head
            y = head.next
            z = head.next.next
            x.next = None
            y.next = None
            a.next = x
            a = a.next
            b.next = y
            b = b.next
            head = z
            
        if head:
            a.next = head
            a = a.next
        
        a.next = bb.next
        return aa.next
            
            
            
            
```

## refs

* [lc](https://leetcode.com/problems/odd-even-linked-list/)
