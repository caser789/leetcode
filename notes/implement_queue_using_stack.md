---
tags: [2019/08/10, data structure/queue, data structure/stack, design, leetcode/232]
title: Implement Queue using Stacks
created: '2019-08-10T09:34:03.356Z'
modified: '2019-08-10T09:35:08.687Z'
---

# Implement Queue using Stacks


Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

### Example:

```
MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
```


> You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
> Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
> You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

## Solution

### method1

```python
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.n = 0
        self.head = None

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        if self.head is None:
            self.head = x
        self.stack1.append(x)
        self.n += 1

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        res = None
        if self.stack2:
            res = self.stack2.pop()
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not res:
            res = self.stack2.pop()
        self.head = self.stack2[-1] if self.stack2 else None
        self.n -= 1
        return res

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.head

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.n
```

### method 2

```python
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack2.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.stack1.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack1[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack1
```
