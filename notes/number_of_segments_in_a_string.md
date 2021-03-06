---
tags: [2020/01/03, leetcode/434]
title: Number of Segments in a String
created: '2019-08-31T09:26:58.869Z'
modified: '2019-11-01T05:11:50.594Z'
---

# Number of Segments in a String

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

### Example:

Input: "Hello, my name is John"
Output: 5

## Solution

```python
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0

        i = 0
        grp = False
        cnt = 0
        while i < n:
            if s[i] != ' ' and not grp:
                grp = True
                cnt += 1

            elif s[i] == ' ' and grp:
                grp = False

            i += 1

        return cnt
```

### better

```python
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = 0
        while i < n and s[i] == ' ':
            i += 1

        if i == n:
            return 0

        cnt = 1
        i += 1
        while i < n:
            if s[i] != ' ' and s[i-1] == ' ':
                cnt += 1
            i += 1
        return cnt
```

## schedule

* [x] 0 2019/09/05
* [x] 1 2019/09/06
* [x] 1 2019/09/09
* [x] 1 2019/09/16
* [x] 1 2019/10/01
* [x] 1 2019/11/01
* [ ] 1 2020/01/03
