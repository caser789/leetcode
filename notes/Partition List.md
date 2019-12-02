---
tags: [2019/11/18, data structure/linked-list, leetcode/86]
title: Partition List
created: '2019-11-18T04:52:44.350Z'
modified: '2019-11-26T13:36:45.043Z'
---

# Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5


## Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        Input: head = 1->4->3->2->5->2, x = 3
        Output: 1->2->2->4->3->5
        """
        i = a = ListNode(None)
        j = b = ListNode(None)

        h = head
        while h:
            nxt = h.next
            h.next = None
            if h.val < x:
                i.next = i = h
            else:
                j.next = j = h
            h = nxt

        i.next = b.next
        return a.next

```

## refs

* [lc](https://leetcode.com/problems/partition-list/)
