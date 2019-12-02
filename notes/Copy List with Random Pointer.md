---
tags: [2019/11/03, data structure/linked-list, leetcode/138]
title: Copy List with Random Pointer
created: '2019-11-01T23:28:47.898Z'
modified: '2019-11-27T07:48:23.720Z'
---

# Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

 ![pic](https://discuss.leetcode.com/uploads/files/1470150906153-2yxeznm.png)

### Example 1:



Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
 

## Note:

You must return the copy of the given head as a reference to the cloned list.

## Solution

```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return
        # round 1
        h = head
        while h:
            node = Node(h.val, h.next, None)
            h.next = node
            h = node.next
        
        # round 2
        h = head
        while h:
            if h.random:
                h.next.random = h.random.next
            h = h.next.next
        
        # round 3
        i = dummy = Node(None, None, None)
        h = head
        while h:
            node = h.next
            
            h.next = node.next
            
            i.next = node
            i = node
            h = node.next
        
        return dummy.next
        
```

## Schedule

* [x] 2019/11/02
* [ ] 2019/11/03
