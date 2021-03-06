---
tags: [2019/11/05, leetcode/961]
title: N-Repeated Element in Size 2N Array
created: '2019-09-07T08:12:21.094Z'
modified: '2019-10-07T04:59:19.280Z'
---

# N-Repeated Element in Size 2N Array

In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.


### Example 1:

Input: [1,2,3,3]
Output: 3

### Example 2:

Input: [2,1,2,5,3,2]
Output: 2

### Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5


## Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even


## Solution

### intuitive

```python
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                return A[i]

```

### knack

```python
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for k in range(1, 4):
            for i in range(len(A)-k):
                if A[i] == A[i+k]:
                    return A[i]
```

## schedule

* [x] 0 2019/09/09
* [x] 1 2019/09/10
* [x] 1 2019/09/13
* [x] 1 2019/09/20
* [x] 1 2019/10/05
* [ ] 1 2019/11/05
