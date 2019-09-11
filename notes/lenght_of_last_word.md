---
tags: [2019/09/16, leetcode/58]
title: Length of Last Word
created: '2019-08-31T09:33:29.772Z'
modified: '2019-09-09T13:22:42.960Z'
---

# Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

### Example:

Input: "Hello World"
Output: 5

## Solution

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        j = n - 1
        while j >= 0 and s[j] == ' ':
            j -= 1
        cnt = 0
        while j >= 0:
            if s[j] == ' ':
                return cnt
            cnt += 1
            j -= 1
        return cnt
```

## schedule

* [x] 0 2019/09/05
* [x] 1 2019/09/06
* [x] 1 2019/09/09
* [ ] 1 2019/09/16
