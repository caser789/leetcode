---
tags: [2019/08/10, data structure/stack, leetcode/20]
title: Valid Parentheses
created: '2019-08-10T05:54:56.668Z'
modified: '2019-08-10T05:55:53.168Z'
---

# Valid Parentheses


Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

### Example 1:

Input: "()"
Output: true

### Example 2:

Input: "()[]{}"
Output: true

### Example 3:

Input: "(]"
Output: false

### Example 4:

Input: "([)]"
Output: false

### Example 5:

Input: "{[]}"
Output: true

## Solution

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        store = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if store[prev] != c:
                    return False
        return not stack
```
