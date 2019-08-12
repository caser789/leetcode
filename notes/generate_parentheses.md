---
tags: [2019/08/12]
title: Generate Parentheses
created: '2019-08-12T12:07:55.931Z'
modified: '2019-08-12T12:08:10.831Z'
---

# Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

## Solution

```python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.backtrack(res, '', n, n)
        return res

    def backtrack(self, res, tmp, left, right):
        if left == 0 and right == 0:
            res.append(tmp)
            return
        if left > 0:
            self.backtrack(res, tmp+'(', left-1, right)
        if right > 0 and right > left:
            self.backtrack(res, tmp+')', left, right-1)
```
