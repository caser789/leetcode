---
tags: [2019/11/19, data structure/monoqueue, leetcode/856]
title: Score of Parentheses
created: '2019-11-19T13:27:16.297Z'
modified: '2019-11-21T01:16:26.738Z'
---

# Score of Parentheses

Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6
 

Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50

## Solution

```python
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for c in S:
            if c == '(':
                stack.append(c)
            elif stack[-1] == '(':
                stack.pop()
                stack.append(1)
            else:
                done = False
                v = 0
                while not done:
                    i = stack.pop()
                    if i == '(':
                        stack.append(v*2)
                        done = True
                    else:
                        v += i
        return sum(stack)

```

## refs

* [lc](https://leetcode.com/problems/score-of-parentheses/)

