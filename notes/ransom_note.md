---
tags: [2019/09/07, leetcode/383]
title: Ransom Note
created: '2019-08-31T09:08:58.787Z'
modified: '2019-09-04T05:54:40.158Z'
---

# Ransom Note

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

## Note:

You may assume that both strings contain only lowercase letters.

```
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
```

## Solution

### index

```python
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        res = [0] * 26

        for c in magazine:
            i = ord(c) - ord('a')
            res[i] += 1

        for c in ransomNote:
            i = ord(c) - ord('a')
            if res[i] == 0:
                return False
            res[i] -= 1

        return True
```

## schedule

* [x] 0 2019/09/03
* [x] 1 2019/09/04
* [ ] 1 2019/09/07
