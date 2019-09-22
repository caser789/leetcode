---
tags: [2019/09/29, data structure/map, leetcode/387, method/index, method/search/hash]
title: First Unique Character in a String
created: '2019-07-30T15:47:11.693Z'
modified: '2019-09-16T15:03:24.600Z'
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

### index

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
        res = [0] * 26
        
        for c in s:
            i = ord(c) - ord('a')
            res[i] += 1
        
        for j, c in enumerate(s):
            i = ord(c) - ord('a')
            if res[i] == 1:
                return j
        return -1
```

## schedule

* [x] 0 2019/09/03
* [x] 1 2019/09/04
* [x] 1 2019/09/07
* [x] 1 2019/09/14
* [ ] 1 2019/09/29
