---
tags: [2019/08/10, data structure/stack, leetcode/150]
title: Evaluate Reverse Polish Notation
created: '2019-08-10T08:01:47.200Z'
modified: '2019-08-10T08:15:17.011Z'
---

# Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.


> Division between two integers should truncate toward zero.
> The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.

### Example 1:

```
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

### Example 2:

```
Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

### Example 3:

```
Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```


## Solution

```python
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        >>> tokens = ["2", "1", "+", "3", "*"]
        >>> Solution().evalRPN(tokens)
        9
        >>> tokens = ["4", "13", "5", "/", "+"]
        >>> Solution().evalRPN(tokens)
        6
        >>> tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        >>> Solution().evalRPN(tokens)
        22
        """
        stack = []
        for token in tokens:
            if token == '+':
                j = stack.pop()
                i = stack.pop()
                stack.append(i + j)
            elif token == '-':
                j = stack.pop()
                i = stack.pop()
                stack.append(i - j)
            elif token == '*':
                j = stack.pop()
                i = stack.pop()
                stack.append(i * j)
            elif token == '/':
                j = stack.pop()
                i = stack.pop()
                if i * j < 0:
                    n = abs(i) / abs(j) * -1
                else:
                    n = i / j
                stack.append(n)
            else:
                stack.append(int(token))
        return stack[-1]
```
