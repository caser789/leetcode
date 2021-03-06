---
tags: [2019/08/20, leetcode/1013]
title: Partition Array Into Three Parts With Equal Sum
created: '2019-08-20T15:17:05.829Z'
modified: '2019-08-20T15:17:25.341Z'
---

# Partition Array Into Three Parts With Equal Sum

Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])


### Example 1:

```
Input: [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
```

### Example 2:

```
Input: [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
```

### Example 3:

```
Input: [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
```


> 3 <= A.length <= 50000
> -10000 <= A[i] <= 10000


## Solution

```python
class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        s = sum(A)
        if s % 3 != 0: return False
        cnt = 0
        part = 0
        for num in A:
            part += num
            if part * 3 != s: continue
            cnt += 1
            if cnt == 2: return True
            part = 0
        return False
```
