---
tags: [2019/11/19, data structure/linked-list, data structure/stack, leetcode/25, method/reverse]
title: Reverse Nodes in k-Group
created: '2019-11-18T13:54:33.673Z'
modified: '2019-11-27T04:02:41.242Z'
---

# Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.

## Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k == 1:
            return head
        dummy = ListNode(None)
        dummy.next = head
        begin = dummy
        i = 0
        while head:
            i += 1
            if i % k == 0:
                begin = reverse(begin, head.next)
                head = begin.next
            else:
                head = head.next
        return dummy.next
        
        
def reverse(begin, end):
    first = cur = begin.next
    prev = begin
    while cur is not end:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    first.next = end
    begin.next = prev
    return first
        
        
```

### stack

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        d = dummy = ListNode(0)
        stack = []
        while head:
            nxt = head.next
            
            if len(stack) < k:
                stack.append(head)
            
            if len(stack) == k:
            
                while stack:
                    n = stack.pop()
                    d.next = n
                    d = d.next
                    
            head = nxt
        
        for n in stack:
            d.next = n
            d = d.next
        
        d.next = None
        return dummy.next
        
        
        
```

## refs

* [lc](https://leetcode.com/problems/reverse-nodes-in-k-group/)

