---
tags: [2019/11/26, application/circle-detect, data structure/linked-list, leetcode/142, method/2-pointers]
title: Linked List Cycle II
created: '2019-11-26T14:28:25.938Z'
modified: '2019-11-26T14:30:07.703Z'
---

# Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

![pic](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:
![pic](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:
![pic](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


 

Follow-up:
Can you solve it without using extra space?

## Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        
        x1 + x2 + x3 + x2 
        x1 + x2 + x1 + x2
        """
        if head is None or head.next is None:
            return
        
        f = s = head
        find = False
        while f and f.next:
            f = f.next.next
            s = s.next
            if f is s:
                find = True
                break
        
        if not find:
            return
        
        a = head
        while a is not s:
            a = a.next
            s = s.next
        return a
        
```

## refs

* [lc](https://leetcode.com/problems/linked-list-cycle-ii/)
