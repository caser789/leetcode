---
tags: [2019/11/16, data structure/linked-list, data structure/priority queue, leetcode/23]
title: Merge k Sorted List
created: '2019-10-21T15:12:59.402Z'
modified: '2019-11-26T12:35:10.857Z'
---

# Merge k Sorted List

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6


## Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = dummy = ListNode(None)
        pq = []
        for lst in lists:
            if not lst: continue
            heapq.heappush(pq, (lst.val, lst))
        
        while pq:
            val, lst = heapq.heappop(pq)
            nxt = lst.next
            lst.next = None
            head.next = lst
            head = head.next
            
            if nxt:
                heapq.heappush(pq, (nxt.val, nxt))
        return dummy.next
```

## schedule

* [x] 0 2019/10/21
* [x] 1 2019/10/22
* [x] 1 2019/10/25
* [x] 1 2019/11/01
* [ ] 1 2019/11/16

## refs

* [lc](https://leetcode.com/problems/merge-k-sorted-lists/)

