---
tags: [2019/08/11, leetcode/331]
title: Verify Preorder Serialization of a Binary Tree
created: '2019-08-11T13:30:04.440Z'
modified: '2019-08-11T13:30:28.667Z'
---

# Verify Preorder Serialization of a Binary Tree

One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

```
     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
```

For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

### Example 1:

```
Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
```

### Example 2:

```
Input: "1,#"
Output: false
```

### Example 3:

```
Input: "9,#,#,1"
Output: false
```

## Solution

```python
class Solution(object):
    def _isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        slots = 1

        for node in preorder.split(','):
            # one node takes one slot
            slots -= 1

            # no more slots available
            if slots < 0:
                return False

            # non-empty node creates 2 children slots
            if node != '#':
                slots += 2
        return slots == 0

    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        slots = 1
        prev = None
        for ch in preorder:
            if ch == ',':
                slots -= 1
                if slots < 0:
                    return False
                if prev != '#':
                    slots += 2
            prev = ch
        slots = slots - 1 if ch == '#' else slots + 1
        return slots == 0
```
