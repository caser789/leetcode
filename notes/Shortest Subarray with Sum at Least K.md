---
tags: [2019/11/02, data structure/monoqueue, leetcode/862]
title: Shortest Subarray with Sum at Least K
created: '2019-10-28T09:06:38.998Z'
modified: '2019-10-30T01:34:32.186Z'
---

# Shortest Subarray with Sum at Least K

Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

 

### Example 1:

Input: A = [1], K = 1
Output: 1

### Example 2:

Input: A = [1,2], K = 4
Output: -1

### Example 3:

Input: A = [2,-1,2], K = 3
Output: 3
 

## Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9

## Solution

```python
import collections

class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        prefix = [0]
        for num in A:
            prefix.append(prefix[-1] + num)
        
        res = n+1
        monoq = collections.deque()
        for y, psum in enumerate(prefix):
            while monoq and psum <= prefix[monoq[-1]]:
                monoq.pop()
            
            while monoq and psum - prefix[monoq[0]] >= K: 
                res = min(res, y - monoq.popleft())
            
            monoq.append(y)
        
        return res if res < n + 1 else -1
            
```

## schedule

* [x] 2019/10/28
* [x] 2019/10/29
* [x] 2019/10/30
* [ ] 2019/11/02
