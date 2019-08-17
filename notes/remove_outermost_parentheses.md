---
tags: [2019/08/17, data structure/stack, leetcode/1021]
title: Remove Outermost Parentheses
created: '2019-08-17T03:52:26.946Z'
modified: '2019-08-17T04:08:27.522Z'
---

# Remove Outermost Parentheses

A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

### Example 1:

```
Input: "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
```

### Example 2:

```
Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
```

### Example 3:

```
Input: "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
```


> S.length <= 10000
> S[i] is "(" or ")"
> S is a valid parentheses string

## Solution

```python
class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return S

        stack = []
        left = 0
        right = 0
        res = []
        for c in S:
            if c == '(':
                left += 1
            else:
                right += 1
            stack.append(c)
            if left and left == right:
                for i in range(1, len(stack)-1):
                    res.append(stack[i])
                stack = []
                left = 0
                right = 0
        return ''.join(stack)
```
