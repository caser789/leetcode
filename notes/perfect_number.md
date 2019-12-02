---
tags: [2019/11/06, leetcode/507]
title: Perfect Number
created: '2019-09-24T15:18:54.896Z'
modified: '2019-10-30T04:47:41.997Z'
---

# Perfect Number


We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)

## Solution

```python
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        
        s = 0
        i = 1
        while i * i <= num:
            if num % i == 0:
                s += i
                if i * i != num:
                    s += num / i
            i += 1
        return s - num == num
        
```

## schedule

* [x] 0 2019/09/30
* [x] 1 2019/10/01
* [x] 1 2019/10/04
* [x] 1 2019/10/11
* [x] 1 2019/10/26
* [x] 1 2019/10/27
* [x] 1 2019/10/30
* [ ] 1 2019/11/06
