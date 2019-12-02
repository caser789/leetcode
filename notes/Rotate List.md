---
tags: [2019/11/19, data structure/linked-list, leetcode/61, method/2-pointers]
title: Rotate List
created: '2019-11-18T13:05:38.950Z'
modified: '2019-11-26T13:32:29.973Z'
---

# Rotate List

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

## Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        1 2 3 4 5
            f f f
        s s s
        """
        if head is None:
            return
        if head.next is None:
            return head
        if not k:
            return head
        
        n = 0
        h = head
        while h:
            n += 1
            h = h.next
        
        k = k % n
        if not k:
            return head
        f = s = head
        for i in range(k):
            f = f.next
        p = None
        while f:
            f = f.next
            s = s.next
            if p is None:
                p = head
            else:
                p = p.next
        
        p.next = None
        ss = s
        while ss.next:
            ss = ss.next
        ss.next = head
        return s
        
        
```

### better

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        
        f   f f f
        s s s
        1 2 3 4 5
        """
        if head is None or head.next is None:
            return head
        if not k:
            return head
        n = 0
        h = head
        while h:
            n += 1
            h = h.next
        
        k = k % n
        if not k:
            return head
        
        fast = slow = head
        for _ in range(k):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        a = b = slow.next
        slow.next = None
        while b.next:
            b = b.next
        b.next = head
        return a
        
```

## refs

* [lc](https://leetcode.com/problems/rotate-list/)
