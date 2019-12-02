---
tags: [2019/11/17, data structure/linked-list, data structure/monoqueue, data structure/stack, leetcode/1019]
title: Next Greater Node In Linked List
created: '2019-11-17T09:00:20.167Z'
modified: '2019-11-26T14:51:46.500Z'
---

# Next Greater Node In Linked List

We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, node_2, node_3, ... etc.

Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.

Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.

 

Example 1:

Input: [2,1,5]
Output: [5,5,0]
Example 2:

Input: [2,7,4,3,5]
Output: [7,0,5,5,0]
Example 3:

Input: [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]
 

Note:

1 <= node.val <= 10^9 for each node in the linked list.
The given list has length in the range [0, 10000].

## Solution

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        kv = {}
        
        h = head
        stack = []
        i = 0
        while h:
            while stack and stack[-1][1] < h.val:
                j, v = stack.pop()
                kv[j] = h.val
            stack.append((i, h.val))
        
            h = h.next
            i += 1
        
        h = head
        i = 0
        res = []
        while h:
            res.append(kv.get(i, 0))
            h = h.next
            i += 1
        return res
            
```

### list + stack

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        h = head
        n = 0
        while h:
            n += 1
            h = h.next
        
        res = [0] * n
        
        h = head
        stack = []
        i = 0
        while h:
            while stack and stack[-1][1] < h.val:
                j, v = stack.pop()
                res[j] = h.val
            stack.append((i, h.val))
            i += 1
            h = h.next
        return res
        
```

## refs

* [lc](https://leetcode.com/problems/next-greater-node-in-linked-list/)
