---
tags: [2019/09/25, leetcode/203, method/2 pointers/linked list]
title: Remove Linked List Elements
created: '2019-09-07T09:16:39.161Z'
modified: '2019-09-22T04:05:13.790Z'
---

# Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

### Example:

```
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
```

## Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        Input:  1->2->6->3->4->5->6, val = 6
        Output: 1->2->3->4->5
        """
        dummy = ListNode(None)
        dummy.next = head
        d = head
        prev = dummy
        while d:
            if d.val == val:
                prev.next = d.next
                d = d.next
            else:
                prev = d
                d = d.next
        return dummy.next
```


## schedule

* [x] 0 2019/09/14
* [x] 1 2019/09/15
* [x] 1 2019/09/18
* [ ] 1 2019/09/25
