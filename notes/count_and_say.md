---
tags: [2019/09/30, application/array/status, leetcode/38]
title: Count and Say
created: '2019-08-31T09:21:26.026Z'
modified: '2019-09-17T14:10:51.326Z'
---

# Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:

```
1.     1
2.     11
3.     21
4.     1211
5.     111221
```

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.


### Example 1:

Input: 1
Output: "1"

### Example 2:

Input: 4
Output: "1211"


## Solution

```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n-1):
            s = count(s)
        return s


def count(s):
    res = []
    cnt = 0
    v = 0

    for c in s:
        if c == v:
            cnt += 1
        else:
            if cnt > 0:
                res.append(str(cnt))
                res.append(v)
            cnt = 1
            v = c

    if cnt > 0:
        res.append(str(cnt))
        res.append(v)
    return ''.join(res)
```

### better

```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        v = '1'
        for i in range(n-1):
            v = count(v)
        return v

def count(chars):
    res = []
    cnt = 0
    v = None
    for c in chars:
        if v is None:
            v = c
            cnt = 1
        elif v == c:
            cnt += 1
        else:
            res.append(str(cnt))
            res.append(v)
            v = c
            cnt = 1

    res.append(str(cnt))
    res.append(c)
    return ''.join(res)
```

## schedule

* [x] 0 2019/09/04
* [x] 1 2019/09/05
* [x] 1 2019/09/08
* [x] 1 2019/09/15
* [ ] 1 2019/09/30
