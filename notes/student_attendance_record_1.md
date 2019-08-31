---
tags: [2019/09/03, leetcode/551, TODO]
title: Student Attendance Record I
created: '2019-08-31T09:13:55.004Z'
modified: '2019-08-31T09:14:09.884Z'
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

```
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """

```
