---
tags: [2019/09/28, leetcode/788]
title: Rotated Digits
created: '2019-08-31T08:59:14.799Z'
modified: '2019-09-15T04:32:44.034Z'
---

# Rotated Digits

X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

### Example:

Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

## Note:

* N  will be in range [1, 10000].


## Solution

```python
kv = {
    '0': '0',
    '1': '1',
    '2': '5',
    '5': '2',
    '6': '9',
    '8': '8',
    '9': '6',
}

def rotate(n):
    n = str(n)
    res = []
    for c in n:
        if c not in kv:
            return False
        res.append(kv[c])
    m = ''.join(res)
    if n == m:
        return False
    return True

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        cnt = 0
        for i in range(1, N+1):
            if rotate(str(i)):
                cnt += 1
        return cnt
```

## schedule

* [x] 0 2019/09/02
* [x] 1 2019/09/03
* [x] 1 2019/09/06
* [x] 1 2019/09/13
* [ ] 1 2019/09/28
