---
tags: [2019/11/19, leetcode/728]
title: Self Dividing Numbers
created: '2019-09-22T11:08:15.796Z'
modified: '2019-10-19T13:33:51.110Z'
---

# Self Dividing Numbers

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

### Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

## Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.

## Solution

```python
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = [i for i in range(left, right+1) if is_self(i)]

def is_self(n):
    res = []
    m = n
    while n > 0:
        n, c = divmod(n, 10)
        if c == 0:
            return False
        if m % c != 0:
            return False
    return True
```


## schedule

* [x] 0 2019/09/23
* [x] 1 2019/09/24
* [x] 1 2019/09/27
* [x] 1 2019/10/04
* [x] 1 2019/10/19
* [ ] 1 2019/11/19
