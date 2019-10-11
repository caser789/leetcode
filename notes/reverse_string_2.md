---
tags: [2019/10/28, leetcode/541]
title: Reverse String II
created: '2019-08-31T09:12:28.918Z'
modified: '2019-09-27T05:12:46.982Z'
---

# Reverse String II

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

### Example:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"

## Restrictions:

> The string consists of lower English letters only.
> Length of the given string and k will in the range [1, 10000]

## Solution

```python
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        a = list(s)
        for i in range(0, len(s), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return ''.join(a)
```

## schedule

* [x] 0 2019/09/03
* [x] 1 2019/09/04
* [x] 1 2019/09/05
* [x] 1 2019/09/12
* [x] 1 2019/09/27
* [ ] 1 2019/10/28
