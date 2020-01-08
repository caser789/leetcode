---
tags: [2019/12/04, leetcode/1004, method/sliding-window]
title: Max Consecutive Ones III
created: '2019-12-04T05:04:25.564Z'
modified: '2019-12-04T05:24:42.849Z'
---

# Max Consecutive Ones III

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

 

### Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

### Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
 

### Note:

1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1 

## Solution

```python
class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        3   4
          3   1
          
          2   3   2   4
        2   2   1   3
        """
        n = len(A)
        i = 0
        for j in range(n):
            K -= 1 - A[j]
            if K < 0:
                K += 1 - A[i]
                i += 1
        
        return j - i + 1

```

## refs

* [dis](https://leetcode.com/problems/max-consecutive-ones-iii/discuss/247564/JavaC%2B%2BPython-Sliding-Window)
* [lc](https://leetcode.com/problems/max-consecutive-ones-iii/)

