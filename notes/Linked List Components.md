---
tags: [2019/11/17, data structure/linked-list, leetcode/817, method/3-while]
title: Linked List Components
created: '2019-11-17T11:13:16.923Z'
modified: '2019-11-27T03:32:51.649Z'
---

# Linked List Components

We are given head, the head node of a linked list containing unique integer values.

We are also given the list G, a subset of the values in the linked list.

Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.

Example 1:

Input: 
head: 0->1->2->3
G = [0, 1, 3]
Output: 2
Explanation: 
0 and 1 are connected, so [0, 1] and [3] are the two connected components.
Example 2:

Input: 
head: 0->1->2->3->4
G = [0, 3, 1, 4]
Output: 2
Explanation: 
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
Note:

If N is the length of the linked list given by head, 1 <= N <= 10000.
The value of each node in the linked list will be in the range [0, N - 1].
1 <= G.length <= 10000.
G is a subset of all values in the linked list.


## Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        s = set(G)
        cnt = 0
        h = head
        while h:
            if h.val in s:
                cnt += 1
                while h.next and h.next.val in s:
                    h = h.next
                
            h = h.next
        return cnt   
```

## refs

* [lc](https://leetcode.com/problems/linked-list-components/)

