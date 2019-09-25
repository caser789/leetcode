---
tags: [2019/10/08, leetcode/242]
title: Valid Anagram
created: '2019-09-07T08:36:24.334Z'
modified: '2019-09-23T14:42:24.984Z'
---

# Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

### Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

### Example 2:

Input: s = "rat", t = "car"
Output: false

## Note:
You may assume the string contains only lowercase alphabets.

## Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?


## Solution

```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lst = [0] * 26
        for c in s:
            i = ord(c) - ord('a')
            lst[i] += 1
        for c in t:
            i = ord(c) - ord('a')
            lst[i] -= 1
        for i in lst:
            if i != 0:
                return False
        return True
```

## schedule

* [x] 0 2019/09/12
* [x] 1 2019/09/13
* [x] 1 2019/09/16
* [x] 1 2019/09/23
* [ ] 1 2019/10/08
