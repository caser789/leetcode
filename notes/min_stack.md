---
tags: [2019/08/10, data structure/stack, design, leetcode/155]
title: Min Stack
created: '2019-08-10T04:57:52.524Z'
modified: '2019-08-10T05:22:44.956Z'
---

# Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


### Example:

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
```


## Solution

```python
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self.lst = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.min is None or x <= self.min:
            self.lst.append(self.min)
            self.min = x
        self.lst.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if not self.lst:
            return
        res = self.lst.pop()
        if res == self.min:
            self.min = self.lst.pop()
        return res

    def top(self):
        """
        :rtype: int
        """
        if not self.lst:
            return
        return self.lst[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
```
