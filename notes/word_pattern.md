---
tags: [2019/11/10, leetcode/290]
title: Word Pattern
created: '2019-09-07T09:00:37.754Z'
modified: '2019-10-10T16:39:27.886Z'
---

# Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

### Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true

### Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false

### Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

### Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false

## Notes:

You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

## Solution

```python
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(' ')
        n = len(pattern)
        m = len(words)
        if n != m:
            return False
        kv = {}
        vk = {}
        for i in range(n):
            word = words[i]
            c = pattern[i]
            if word not in kv:
                kv[word] = c
            elif kv[word] != c:
                return False
            if c not in vk:
                vk[c] = word
            elif vk[c] != word:
                return False
        return True
```


## schedule

* [x] 0 2019/09/14
* [x] 1 2019/09/15
* [x] 1 2019/09/18
* [x] 1 2019/09/25
* [x] 1 2019/10/10
* [ ] 1 2019/11/10
