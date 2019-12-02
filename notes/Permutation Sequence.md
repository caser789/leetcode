---
tags: [2019/11/16, application/permutation, leetcode/60, method/backtrack]
title: Permutation Sequence
created: '2019-11-16T09:16:56.036Z'
modified: '2019-11-24T10:06:24.182Z'
---

# Permutation Sequence

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

## Solution

```python
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        factorial = [1]
        for i in range(1, n+1):
            factorial.append(factorial[-1]*i)

        nums = range(1, n+1)
        res = 0

        k -= 1

        while n:
            fac = factorial[n-1]
            i, k = divmod(k, fac)
            res = res * 10 + nums[i]
            nums.pop(i)
            n -= 1
        return str(res)

```

## refs

* [lc](https://leetcode.com/problems/permutation-sequence/)

