---
tags: [2019/11/06, leetcode/908]
title: Smallest Range I
created: '2019-10-08T14:54:37.090Z'
modified: '2019-10-22T05:22:27.237Z'
---

# Smallest Range I

Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.

 

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]
Example 3:

Input: A = [1,3,6], K = 3
Output: 0
Explanation: B = [3,3,3] or B = [4,4,4]
 

## Note:

1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000

## Solution

```python
class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        x = max(A)
        y = min(A)
        
        x = x - K
        y = y + K
        
        return max(0, x-y)
        
```


## schedule

* [x] 0 2019/10/11
* [x] 1 2019/10/12
* [x] 1 2019/10/15
* [x] 1 2019/10/22
* [ ] 1 2019/11/06

