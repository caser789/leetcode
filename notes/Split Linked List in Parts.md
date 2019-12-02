---
tags: [2019/11/17, data structure/linked-list, leetcode/725, method/divmod]
title: Split Linked List in Parts
created: '2019-11-17T12:07:28.611Z'
modified: '2019-11-27T07:17:00.284Z'
---

# Split Linked List in Parts

Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
Example 1:
Input:
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].
Example 2:
Input: 
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
Note:

The length of root will be in the range [0, 1000].
Each value of a node in the input will be an integer in the range [0, 999].
k will be an integer in the range [1, 50].

## Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        cur = root
        cnt = 0
        while cur:
            cnt += 1
            cur = cur.next
        width, remainder = divmod(cnt, k)
        
        res = []
        cur = root
        for i in range(k):
            head = write = ListNode(None)
            for j in range(width+(i<remainder)):
                write.next = write = ListNode(cur.val)
                if cur:
                    cur = cur.next
            res.append(head.next)
        return res
```


### in-place

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        cnt = 0
        h = root
        while h:
            cnt += 1
            h = h.next
        width, remain = divmod(cnt, k)
        
        res = []
        cur = root
        for i in range(k):
            head = cur
            for j in range(width+(i<remain)-1):
                if cur:
                    cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            res.append(head)
        return res
```

## refs

* [lc](https://leetcode.com/problems/split-linked-list-in-parts/)

