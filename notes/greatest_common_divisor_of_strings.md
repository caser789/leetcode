---
tags: [2019/09/13, application/gcd, leetcode/1071]
title: Greatest Common Divisor of Strings
created: '2019-08-31T09:01:01.319Z'
modified: '2019-09-06T14:20:41.969Z'
---

# Greatest Common Divisor of Strings

For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.


### Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

### Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

### Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


## Note:

> 1 <= str1.length <= 1000
> 1 <= str2.length <= 1000
> str1[i] and str2[i] are English uppercase letters.

## Solution

```python
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        if not str1.startswith(str2):
            return ''
        if not str2:
            return str1
        return self.gcdOfStrings(str1[len(str2):], str2)
```

## schedule

* [x] 0 2019/09/02
* [x] 1 2019/09/03
* [x] 1 2019/09/06
* [ ] 1 2019/09/13

