---
tags: [2019/11/01, leetcode/58]
title: Length of Last Word
created: '2019-08-31T09:33:29.772Z'
modified: '2019-10-02T14:39:32.281Z'
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
        i = n - 1
        
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        res = 0
        while i >= 0 and s[i] != ' ':
            i -= 1
            res += 1
        return res
```

## schedule

* [x] 0 2019/09/05
* [x] 1 2019/09/06
* [x] 1 2019/09/09
* [x] 1 2019/09/16
* [x] 1 2019/10/01
* [ ] 1 2019/11/01
