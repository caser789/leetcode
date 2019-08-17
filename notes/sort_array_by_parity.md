---
tags: [2019/08/17, leetcode/905, method/sort/quick]
title: Sort Array By Parity
created: '2019-08-17T05:25:53.502Z'
modified: '2019-08-17T05:26:49.408Z'
---

# Sort Array By Parity

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

### Example 1:

```
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
```

> 1 <= A.length <= 5000
> 0 <= A[i] <= 5000

## Solution

```python
class Solution(object):
    def sortArrayByParity(self, lst):
        """
        :type lst: List[int]
        :rtype: List[int]
        """
        n = len(lst)
        if not n:
            return lst

        lo = 0
        hi = n - 1
        while lo < hi:
            while lo < hi and lst[lo] % 2 == 0:
                lo += 1
            while lo < hi and lst[hi] % 2 == 1:
                hi -= 1

            if lo < hi:
                lst[lo], lst[hi] = lst[hi], lst[lo]
            else:
                break
        return lst
```
