---
tags: [2019/11/19, leetcode/921]
title: Minimum Add to Make Parentheses Valid
created: '2019-11-19T13:09:14.668Z'
modified: '2019-11-19T13:09:58.861Z'
---

# Minimum Add to Make Parentheses Valid

Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

 

Example 1:

Input: "())"
Output: 1
Example 2:

Input: "((("
Output: 3
Example 3:

Input: "()"
Output: 0
Example 4:

Input: "()))(("
Output: 4
 

Note:

S.length <= 1000
S only consists of '(' and ')' characters.


## Solution

```python
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        cnt = 0
        for c in S:
            if c == '(':
                stack.append(c)
            elif stack and stack[-1] == '(':
                stack.pop()
            else:
                cnt += 1
        
        return cnt + len(stack)
                
```

## refs

* [lc](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)

