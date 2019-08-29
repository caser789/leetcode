---
tags: [2019/08/29, application/add, leetcode/989]
title: Add to Array-Form of Integer
created: '2019-08-29T15:10:50.940Z'
modified: '2019-08-29T15:11:27.897Z'
---

# Add to Array-Form of Integer

For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.


### Example 1:

```
Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
```

### Example 2:

```
Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
```

### Example 3:

```
Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
```

### Example 4:

```
Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000
```

## Solution

```python
class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        res = []
        n = len(A)
        i = n - 1
        while i >= 0 or K:
            if i >= 0:
                digit = A[i]
            else:
                digit = 0
            K, v = divmod(digit + K, 10)
            res.append(v)
        return res[::-1]
```
