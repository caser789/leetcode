---
tags: [2019/11/18, data structure/linked-list, leetcode/430]
title: Flatten a Multilevel Doubly Linked List
created: '2019-11-18T01:07:54.746Z'
modified: '2019-11-27T13:05:56.269Z'
---

# Flatten a Multilevel Doubly Linked List

You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

 

Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
 

Explanation for the above example:

Given the following multilevel doubly linked list:


 

We should return the following flattened doubly linked list:

![pic](https://assets.leetcode.com/uploads/2018/10/12/multilevellinkedlist.png)
![pic](https://assets.leetcode.com/uploads/2018/10/12/multilevellinkedlistflattened.png)

## solution

```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return head
        
        nxt = head.next
        child = head.child
        head.next = None
        head.child = None
        if nxt:
            nxt.prev = None
        
        nxt = self.flatten(nxt)
        child = self.flatten(child)
        
        h = head
        if child:
            child.prev = h
            h.next = child
        while h.next:
            h = h.next
        h.next = nxt
        if nxt:
            nxt.prev = h
        return head      
```

### stack

```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return head
        
        stack = [head]
        d = dummy = Node(0)
        while stack:
            node = stack.pop()
            if node.next:
                stack.append(node.next)
                node.next = None
            if node.child:
                stack.append(node.child)
                node.child = None
                
            d.next = node
            node.prev = d
            d = d.next
        if dummy.next:
            dummy.next.prev = None
            
        return dummy.next
            
```

## refs

* [lc](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)
