---
tags: [2019/11/19, leetcode/1190]
title: Reverse Substrings Between Each Pair of Parentheses
created: '2019-11-19T04:52:16.992Z'
modified: '2019-11-19T04:53:05.117Z'
---

# Reverse Substrings Between Each Pair of Parentheses

You are given a string s that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 

Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
Example 4:

Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"
 

Constraints:

0 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It's guaranteed that all parentheses are balanced.

## Solution

```python
class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str

        Input: s = "(ed(et(oc))el)"
        Output: "leetcode"
        """
        stack = []
        res = list(s)
        n = len(s)

        def reverse(i, j):
            i += 1
            j -= 1
            while i < j:
                res[i], res[j] = res[j], res[i]
                i += 1
                j -= 1

        for i in range(n):
            if s[i] == '(':
                stack.append(i)
                res[i] = ''
            elif s[i] == ')':
                res[i] = ''
                j = stack.pop()
                reverse(j, i)
        return ''.join(res)

```

## refs

* [lc](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/)

