---
tags: [2019/11/16, application/permutation, leetcode/526, method/backtrack]
title: Beautiful Arrangement
created: '2019-11-16T03:48:15.823Z'
modified: '2019-11-24T10:56:36.905Z'
---

# Beautiful Arrangement

Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
 

Now given N, how many beautiful arrangements can you construct?

Example 1:

Input: 2
Output: 2
Explanation: 

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
 

Note:

N is a positive integer and will not exceed 15.
 

## Solution

```python
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        nums = range(1, N+1)
        
        self.res = 0
        def collect(tmp, seen):
            if len(seen) == N:
                self.res += 1
                return
            
            i = len(tmp) + 1
            for num in nums:
                if num in seen: continue
                
                if i % num and num % i: continue
                    
                tmp.append(num)
                seen.add(num)
                
                collect(tmp, seen)
                
                tmp.pop()
                seen.remove(num)
                
        
        collect([], set())
        
        return self.res
```

### backtrack

```python
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        nums = range(1, N+1)
        
        seen = [False] * (N+1)
        self.count = 0
        
        def search(i):
            if i == N + 1:
                self.count += 1
                return
            
            for num in nums:
                if seen[num]: continue
                
                if i % num == 0 or num % i == 0:
                    
                    seen[num] = True
                    
                    search(i+1)
                    
                    seen[num] = False
                
                
        search(1)
        return self.count
```

## refs

* [lc](https://leetcode.com/problems/beautiful-arrangement/)


