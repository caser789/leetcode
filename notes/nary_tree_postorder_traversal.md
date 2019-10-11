---
tags: [2019/10/13, leetcode/590]
title: N-ary Tree Postorder Traversal
created: '2019-08-31T09:45:05.727Z'
modified: '2019-10-07T15:44:39.732Z'
---

# N-ary Tree Postorder Traversal

Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:

![pic](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)


Return its postorder traversal as: [5,6,3,2,4,1].


## Note:

Recursive solution is trivial, could you do it iteratively?

## Solution

### recursive

```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        def get(node):
            if node is None:
                return
            for c in node.children:
                get(c)

            res.append(node.val)
        get(root)
        return res


```

### itertive

```python
class Solution(object):
    def postorder(self, root):
        if root is None:
            return []
        stack, count, res = [root], [0], []
        while stack:
            while count[-1] < len(stack[-1].children):
                stack.append(stack[-1].children[count[-1]])
                count.append(0)
            res.append(stack.pop().val)
            count.pop()
            if len(count) != 0:
                count[-1] += 1

        return res
```

## schedule

* [x] 0 2019/09/06
* [x] 1 2019/09/07
* [x] 1 2019/09/10
* [x] 1 2019/09/17
* [x] 1 2019/10/02
* [x] 1 2019/10/03
* [x] 1 2019/10/06
* [ ] 1 2019/10/13
