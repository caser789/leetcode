---
tags: [2019/09/28, leetcode/937]
title: Reorder Log Files
created: '2019-08-31T08:57:05.976Z'
modified: '2019-09-15T04:06:23.403Z'
---

# Reorder Log Files

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.


### Example 1:

Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]


## Note:

* 0 <= logs.length <= 100
* 3 <= logs[i].length <= 100
* logs[i] is guaranteed to have an identifier, and a word after the identifier.

## Solution

## intuitive

```python
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """

        def func(a):
            i = a.index(' ')
            if a[i+1].isdigit():
                return chr(ord('z')+1), 1
            return a[i+1:], a[:i]


        return sorted(logs, key=func)
```

## schedule

* [x] 0 2019/09/02
* [x] 1 2019/09/03
* [x] 1 2019/09/06
* [x] 1 2019/09/13
* [ ] 1 2019/09/28
