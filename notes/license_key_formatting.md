---
tags: [2019/10/25, leetcode/482, method/parse]
title: License Key Formatting
created: '2019-09-24T15:13:39.964Z'
modified: '2019-10-10T12:56:22.841Z'
---

# License Key Formatting

You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.

Example 1:
Input: S = "5F3Z-2e-9-w", K = 4

Output: "5F3Z-2E9W"

Explanation: The string S has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:
Input: S = "2-5g-3-J", K = 2

Output: "2-5G-3J"

Explanation: The string S has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
Note:
The length of string S will not exceed 12,000, and K is a positive integer.
String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
String S is non-empty.

## Solution

```python
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        n = len(S)
        lst = []
        tmp = []
        
        
        for i in range(n-1, -1, -1):
            if S[i] == '-': continue
            if len(tmp) == K:
                lst.append(''.join(tmp[::-1]))
                tmp = []
            
            tmp.append(S[i].upper())
        if tmp:
            lst.append(''.join(tmp[::-1]))
            
        
        return '-'.join(lst[::-1])
```

## schedule

* [x] 0 2019/09/29
* [x] 1 2019/09/30
* [x] 1 2019/10/03
* [x] 1 2019/10/10
* [ ] 1 2019/10/25
