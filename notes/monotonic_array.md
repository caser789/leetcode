---
tags: [2019/08/28, leetcode/896]
title: Monotonic Array
created: '2019-08-28T14:17:06.751Z'
modified: '2019-08-28T14:17:25.306Z'
---

# Monotonic Array

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

### Example 1:

```
Input: [1,2,2,3]
Output: true
```

### Example 2:

```
Input: [6,5,4,4]
Output: true
```

### Example 3:

```
Input: [1,3,2]
Output: false
```

### Example 4:

``
Input: [1,2,4,5]
Output: true
``

### Example 5:

```
Input: [1,1,1]
Output: true
```


## Note:

> 1 <= A.length <= 50000
> -100000 <= A[i] <= 100000


## Solution

### Intuition

```python
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        i = 0
        prev = None
        while i < n:
            while i+1 < n and A[i] == A[i+1]:
                i += 1
            if prev is None:
                prev = A[i]
                i += 1
            elif i + 1 < n:
                if prev < A[i] < A[i+1]:
                    i += 1
                    continue
                if prev > A[i] > A[i+1]:
                    i += 1
                    continue
                return False
            else:
                return True
        return True
```

### Better

```python
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        store = 0
        for i in range(len(A)-1):
            c = cmp(A[i], A[i+1])
            if c:
                if not store:
                    store = c
                elif c != store:
                    return False
        return True
```

### Double negation

```python
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increasing = descreasing = True

        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                increasing = False
            if A[i] < A[i+1]:
                descreasing = False

        return increasing or descreasing

```
