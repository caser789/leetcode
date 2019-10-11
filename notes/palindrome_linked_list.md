---
tags: [2019/11/10, leetcode/234]
title: Palindrome Linked List
created: '2019-09-07T09:15:18.422Z'
modified: '2019-10-10T14:00:48.646Z'
---

# Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

### Example 1:

Input: 1->2
Output: false

### Example 2:

Input: 1->2->2->1
Output: true

## Follow up:
Could you do it in O(n) time and O(1) space?


## Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
                i
        1 2 3 4 5
            j

                    i
        1 2 3 4 5 6
              j
        """
        if head is None: return False
        if head.next is None: return True

        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        dummy = ListNode(None)
        while slow:
            a = slow.next
            slow.next = dummy.next
            dummy.next = slow
            slow = a

        i = dummy.next
        j = head
        while i and j:
            if i.val != j.val:
                return False
            i = i.next
            j = j.next
        return True
```

## schedule

* [x] 0 2019/09/14
* [x] 1 2019/09/15
* [x] 1 2019/09/18
* [x] 1 2019/09/25
* [x] 1 2019/10/10
* [ ] 1 2019/11/10
