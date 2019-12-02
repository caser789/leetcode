---
tags: [2019/11/10, application/circle-detect, data structure/linked-list, leetcode/141, method/2-pointers]
title: Linked List Cycle
created: '2019-09-07T09:13:18.859Z'
modified: '2019-11-26T13:58:38.019Z'
---

# Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.



### Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

![pic](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

### Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

![pic](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

### Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

![pic](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)


## Follow up:

Can you solve it using O(1) (i.e. constant) memory?


## Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False

        fast = head.next
        slow = head
        while fast != slow:
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
        return True
```


## schedule

* [x] 0 2019/09/14
* [x] 1 2019/09/15
* [x] 1 2019/09/18
* [x] 1 2019/09/25
* [x] 1 2019/10/10
* [ ] 1 2019/11/10
