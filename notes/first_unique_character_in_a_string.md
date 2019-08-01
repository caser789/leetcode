---
title: First Unique Character in a String
created: '2019-07-30T15:47:11.693Z'
modified: '2019-08-01T05:40:33.985Z'
---

# First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

### Examples:

```
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
```

> You may assume the string contain only lowercase letters.

## Solution

```python
class Solution(object):
    def firstUniqChar(self, s):
        """
        >>> s = "leetcode"
        >>> Solution().firstUniqChar(s)
        0
        >>> s = "loveleetcode"
        >>> Solution().firstUniqChar(s)
        2
        """
        store = {}
        for c in s:
            store.setdefault(c, 0)
            store[c] += 1

        for i, c in enumerate(s):
            if store[c] == 1:
                return i
        return -1
```
