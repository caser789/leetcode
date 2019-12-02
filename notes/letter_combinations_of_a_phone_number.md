---
tags: [2019/08/12, application/combination, leetcode/17, method/backtracking, method/traversal/bfs]
title: Letter Combinations of a Phone Number
created: '2019-08-12T12:17:28.035Z'
modified: '2019-11-23T13:54:30.510Z'
---

# Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![pic](http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

### Example:

```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

```

> Although the above answer is in lexicographical order, your answer could be in any order you want.

## Solution

```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        num_to_chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = []
        self.backtrack(res, digits, '', 0, num_to_chars)
        return res

    def backtrack(self, res, digits, s, index, num_to_chars):
        if len(s) == len(digits):
            res.append(s)
            return

        for c in num_to_chars[digits[index]]:
            self.backtrack(res, digits, s+c, index+1, num_to_chars)
```

### bfs

```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        kv = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        q = ['']
        for digit in digits:
            chars = kv[digit]
            nxt = []
            for s in q:
                for c in chars:
                    nxt.append(s+c)
            q = nxt
        return q
            
```

## refs

* [lc](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

