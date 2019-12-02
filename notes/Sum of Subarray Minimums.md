---
tags: [2019/11/20, data structure/monoqueue, leetcode/907]
title: Sum of Subarray Minimums
created: '2019-11-20T13:33:02.854Z'
modified: '2019-11-21T01:15:58.518Z'
---

# Sum of Subarray Minimums

Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
 

Note:

1 <= A.length <= 30000
1 <= A[i] <= 30000

## Solution

### brute force

```python
class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        s = 0
        for i in range(n):
            for j in range(i, n):
                
                s += min(A[i:j+1])
        
        return s
```

### monostack

```python
class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        mod = 10**9+7
        left = [0] * n
        right = [0] * n
        s1 = []
        s2 = []

        for i in range(n):
            count = 1
            while s1 and s1[-1][0] > A[i]:
                count += s1.pop()[1]
            left[i] = count
            s1.append([A[i], count])

        for i in range(n-1, -1, -1):
            count = 1
            while s2 and s2[-1][0] >= A[i]:
                count += s2.pop()[1]
            right[i] = count
            s2.append([A[i], count])

        return sum(a * l * r for a, l, r in zip(A, left, right)) % mod

```

## refs

* [lc](https://leetcode.com/problems/sum-of-subarray-minimums/)

