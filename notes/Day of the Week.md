---
tags: [2019/10/13, leetcode/1185]
title: Day of the Week
created: '2019-10-08T15:04:43.341Z'
modified: '2019-10-10T12:29:29.115Z'
---

# Day of the Week

Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.

## Solution

### day from 19710101, friday

```python
day_of_month = [
    [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
]
weekday = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]

# 1971, 1, 1 Friday


class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        days = days_from_19710101(day, month, year) - 1
        d = days % 7
        return weekday[d]


def days_from_19710101(day, month, year):
    days = 0
    y = 1971
    while y < year:
        days += days_of_a_year(y)
        y += 1
    days += days_of_a_year_to_today(day, month, year)
    return days


def days_of_a_year(y):
    if is_leap_year(y): return 366
    return 365


def days_of_a_year_to_today(day, month, year):
    leap = int(is_leap_year(year))
    res = 0
    days = day_of_month[leap]
    m = 0
    while m < month-1:
        res += days[m]
        m += 1
    return res + day

def is_leap_year(y):
    if y % 400 == 0:
        return True
    return y % 4 == 0 and y % 100 != 0

print days_of_a_year_to_today(3, 3, 1999)
assert days_from_19710101(3, 3, 1972) == 428
print  days_from_19710101(9, 10, 2019)

```

## schedule

* [x] 0 2019/10/09
* [x] 1 2019/10/10
* [ ] 1 2019/10/13

