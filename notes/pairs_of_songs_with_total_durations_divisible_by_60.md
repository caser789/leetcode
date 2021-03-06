---
tags: [2019/08/21, knack, leetcode/1010]
title: Pairs of Songs With Total Durations Divisible by 60
created: '2019-08-21T12:59:01.373Z'
modified: '2019-08-21T13:12:23.720Z'
---

# Pairs of Songs With Total Durations Divisible by 60

In a list of songs, the i-th song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.


### Example 1:

```
Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
```

### Example 2:

```
Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
```


> 1 <= time.length <= 60000
> 1 <= time[i] <= 500

## Solution

```python
class Solution(object):
    def numPairsDivisibleBy60(self, nums):
        """
        :type time: List[int]
        :rtype: int
        """
        d = {}
        res = 0
        for num in nums:
            other = - num % 60
            res += d.get(other, 0)
            num = num % 60
            d.setdefault(num, 0)
            d[num] += 1
        return res
```
