---
tags: [2019/09/23, leetcode/409]
title: Longest Palindrome
created: '2019-09-07T08:40:56.846Z'
modified: '2019-09-19T05:13:18.702Z'
---

# Longest Palindrome

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

### Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.



## Solution

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        kv = {}
        for c in s:
            kv.setdefault(c, 0)
            kv[c] += 1

        flag = 0
        cnt = 0
        for k, v in kv.items():
            i, j = divmod(v, 2)
            if j:
                flag = 1
            cnt += i * 2
        return cnt + 1 * flag
```

## schedule

* [x] 0 2019/09/12
* [x] 1 2019/09/13
* [x] 1 2019/09/16
* [ ] 1 2019/09/23
