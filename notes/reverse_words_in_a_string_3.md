---
tags: [2019/10/28, leetcode/557, method/2 pointers]
title: Reverse Words in a String III
created: '2019-08-31T08:44:22.506Z'
modified: '2019-09-28T04:48:02.689Z'
---

# Reverse Words in a String III


Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

### Example 1:

Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

> In the string, each word is separated by single space and there will not be any extra space in the string.


## Solution

```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        res = []
        lo = 0
        hi = 0
        for i, c in enumerate(s):
            if c == ' ':
                while hi >= lo:
                    res.append(s[hi])
                    hi -= 1
                res.append(c)
                lo = i + 1
            else:
                hi = i

        while hi >= lo:
            res.append(s[hi])
            hi -= 1

        return ''.join(res)
```

## schedule

* [x] 0 2019/09/01
* [x] 1 2019/09/02
* [x] 3 2019/09/05
* [x] 3 2019/09/12
* [x] 3 2019/09/27
* [ ] 3 2019/10/28
