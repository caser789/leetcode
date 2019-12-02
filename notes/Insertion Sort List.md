---
tags: [2019/11/18, data structure/linked-list, leetcode/147, method/sort/insertion]
title: Insertion Sort List
created: '2019-11-18T05:01:36.723Z'
modified: '2019-11-26T10:54:59.499Z'
---

# Insertion Sort List

Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

![pic](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)

## Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return

        dummy = ListNode(0)
        cur = head
        prev = dummy
        nxt = None

        while cur is not None:
            nxt = cur.next

            while prev.next is not None and prev.next.val < cur.val:
                prev = prev.next

            cur.next = prev.next
            prev.next = cur
            prev = dummy
            cur = nxt
        return dummy.next

```

## refs

* [lc](https://leetcode.com/problems/insertion-sort-list/)

