---
tags: [2019/11/18, data structure/linked-list, leetcode/1171, method/accumulative-sum]
title: Remove Zero Sum Consecutive Nodes from Linked List
created: '2019-11-18T01:40:43.652Z'
modified: '2019-11-27T03:10:52.713Z'
---

# Remove Zero Sum Consecutive Nodes from Linked List

Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

 

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]
 

Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.

## Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return

        d = dummy = ListNode(0)
        dummy.next = head
        sum_to_node = {0: dummy}

        s = 0
        while head:
            s += head.val
            if s in sum_to_node:
                p = prev = sum_to_node[s]

                ss = s
                while prev.next is not head:
                    prev = prev.next
                    ss += prev.val
                    sum_to_node.pop(ss)
                p.next = head.next

            else:
                sum_to_node[s] = head
            head = head.next


        return dummy.next


```

## refs

* [lc](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/)
