---
tags: [2019/08/10, data structure/queue, data structure/stack, leetcode/225]
title: Implement Stack using Queues
created: '2019-08-10T10:00:29.409Z'
modified: '2019-08-10T10:01:12.714Z'
---

# Implement Stack using Queues


Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.

### Example:

```
MyStack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
```


> You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
> Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
> You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).


## Solution

```python
from collections import deque

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.n = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        for i in range(self.n):
            self.queue.append(self.queue.popleft())
        self.n += 1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        self.n -= 1
        return self.queue.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```
