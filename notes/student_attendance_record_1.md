---
tags: [2019/09/29, application/array/status, leetcode/551]
title: Student Attendance Record I
created: '2019-08-31T09:13:55.004Z'
modified: '2019-09-17T05:13:22.436Z'
---

# Student Attendance Record I

You are given a string representing an attendance record for a student. The record only contains the following three characters:

```
'A' : Absent.
'L' : Late.
'P' : Present.
```

A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

### Example 1:

Input: "PPALLP"
Output: True

### Example 2:

Input: "PPALLL"
Output: False

## Solution

```python
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count_A = 0
        count_L = 0
        for c in s:

            if c == 'A':
                count_L = 0
                count_A += 1
                if count_A > 1:
                    return False

            elif c == 'L':
                count_L += 1
                if count_L > 2:
                    return False
            else:
                count_L = 0

        return True

```

## schedule

* [x] 0 2019/09/03
* [x] 1 2019/09/04
* [x] 1 2019/09/07
* [x] 1 2019/09/14
* [ ] 1 2019/09/29
