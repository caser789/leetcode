---
tags: [2019/08/12, leetcode/401, TODO]
title: Binary Watch
created: '2019-08-12T13:33:55.567Z'
modified: '2019-08-12T14:24:30.970Z'
---

# Binary Watch

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

![pic](https://upload.wikimedia.org/wikipedia/commons/8/8b/Binary_clock_samui_moon.jpg)

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

### Example:

```
Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
```

> The order of output does not matter.
> The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
> The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

## Solution

```python
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
```