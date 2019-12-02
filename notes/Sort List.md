---
tags: [2019/11/03, data structure/linked-list, leetcode/148, method/sort/merge]
title: Sort List
created: '2019-11-02T13:01:34.067Z'
modified: '2019-11-26T12:04:32.161Z'
---

# Sort List

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

## Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        
         pre
            1 
               2
        4 2 1 3
        """
        if head is None or head.next is None:
            return head
        
        p1 = p2 = pre = head
        while p2 and p2.next:
            pre = p1
            p1 = p1.next
            p2 = p2.next.next
        
        pre.next = None
        
        h1 = self.sortList(head)
        h2 = self.sortList(p1)
        
        return self.merge(h1, h2)
    
    def merge(self, h1, h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1
        
        if h1.val < h2.val:
            h1.next = self.merge(h1.next, h2)
            return h1
        h2.next = self.merge(h2.next, h1)
        return h2
        
        
```

## schedule

* [x] 2019/11/02
* [ ] 2019/11/03

## refs

* [lc](https://leetcode.com/problems/sort-list/)
