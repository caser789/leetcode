---
tags: [2019/09/09, leetcode/125, method/2 pointers, method/3 while]
title: Valid Palindrome
created: '2019-08-31T09:34:49.507Z'
modified: '2019-09-06T15:18:27.117Z'
---

# Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

### Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

### Example 2:

Input: "race a car"
Output: false

## Solution

```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        i = 0
        j = n - 1
        done = False
        ss = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
        while i < j and not done:
            while i < j and s[i] not in ss:
                i += 1
            while i < j and s[j] not in ss:
                j -= 1

            if i >= j:
                done = True
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1

        return True
```

## schedule

* [x] 0 2019/09/05
* [x] 1 2019/09/06
* [ ] 1 2019/09/09
