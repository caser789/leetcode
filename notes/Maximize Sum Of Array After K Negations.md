---
tags: [2019/10/09, leetcode/1005]
title: Maximize Sum Of Array After K Negations
created: '2019-10-08T14:57:50.313Z'
modified: '2019-10-08T14:58:23.273Z'
---

# Maximize Sum Of Array After K Negations

Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)

Return the largest possible sum of the array after modifying it in this way.

 

Example 1:

Input: A = [4,2,3], K = 1
Output: 5
Explanation: Choose indices (1,) and A becomes [4,-2,3].
Example 2:

Input: A = [3,-1,0,2], K = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
Example 3:

Input: A = [2,-3,-1,5,-4], K = 2
Output: 13
Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].
 

## Note:

1 <= A.length <= 10000
1 <= K <= 10000
-100 <= A[i] <= 100

## Solution

```python
class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
```
