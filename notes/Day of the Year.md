---
tags: [2019/10/13, leetcode/1154]
title: Day of the Year
created: '2019-10-08T15:02:58.193Z'
modified: '2019-10-10T12:33:16.744Z'
---

# Day of the Year

Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

 

Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41
Example 3:

Input: date = "2003-03-01"
Output: 60
Example 4:

Input: date = "2004-03-01"
Output: 61
 

Constraints:

date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.

## Solution

```python
days_by_month = [
    [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
]


class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year, month, day = date.split('-')
        year, month, day = int(year), int(month), int(day)
        i = is_leap_year(year)
        days = days_by_month[i]
        cnt = 0
        m = 0
        while m < month-1:
            cnt += days[m]
            m += 1
        cnt += day
        return cnt


def is_leap_year(year):
    if year % 400 == 0: return True
    return year % 4 == 0 and year % 100 != 0


print Solution().dayOfYear('2019-01-09')

        
```

## schedule

* [x] 0 2019/10/09
* [x] 1 2019/10/10
* [ ] 1 2019/10/13

