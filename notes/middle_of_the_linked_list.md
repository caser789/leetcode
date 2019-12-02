---
tags: [2019/11/10, data structure/linked-list, leetcode/876, method/2 pointers/fast and slow, method/2-pointers]
title: Middle of the Linked List
created: '2019-09-07T09:07:24.677Z'
modified: '2019-11-26T14:44:39.951Z'
---

# Middle of the Linked List

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.



### Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

### Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.


## Note:

The number of nodes in the given list will be between 1 and 100.


## Solution

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        a = b = head
        while a.next and b.next:
            a = a.next
            b = b.next
            if b.next:
                b = b.next
        return a
```

## schedule

* [x] 0 2019/09/14
* [x] 1 2019/09/15
* [x] 1 2019/09/18
* [x] 1 2019/09/25
* [x] 1 2019/10/10
* [ ] 1 2019/11/10

## refs

* [lc](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/)

