---
tags: [2019/09/26, leetcode/852]
title: Peak Index in a Mountain Array
created: '2019-09-07T09:34:26.873Z'
modified: '2019-09-22T06:59:13.450Z'
---

# Peak Index in a Mountain Array

Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

### Example 1:

Input: [0,1,0]
Output: 1

### Example 2:

Input: [0,2,1,0]
Output: 1

## Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.

## Solution

### intuitive

```python
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return False

        v = A[0]
        i = 1
        done = False
        while not done and i < n:
            if A[i] > v:
                v = A[i]
                i += 1
            elif A[i] == v:
                return False
            else:
                done = True
        if v == A[0]:
            return False
        max_index = i - 1

        while i < n:
            if A[i] >= A[i-1]:
                return False
            i += 1
        return max_index
```

### binary

```python
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        i = 0
        j = n - 1
        while i < j:
            mi = (i+j)/2
            if A[mi] < A[mi+1]:
                i = mi + 1
            else:
                j = mi
        return i
```


## schedule

* [x] 0 2019/09/15
* [x] 1 2019/09/16
* [x] 1 2019/09/19
* [ ] 1 2019/09/26
