---
tags: [2019/11/16, leetcode/89]
title: Gray Code
created: '2019-11-16T05:13:56.213Z'
modified: '2019-11-25T03:24:58.316Z'
---

# Gray Code

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].

## Solution

```python
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def _sum(lst):
            s = 0
            for num in lst:
                s = s * 2 + num
            return s
            
        res = []
        
        def collect(tmp, seen):
            s = _sum(tmp)
            res.append(s)
            seen.add(s)
                        
            for i in range(n):
                tmp[i] = 1-tmp[i]
                s = _sum(tmp)
                if s  in seen:
                    tmp[i] = 1-tmp[i]
                    continue
                else:
                    collect(tmp, seen)
                    break
               
        
        tmp = [0] * n
        seen = set()        
        collect(tmp, seen)
        return res
```

### trick

```python
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        size = 1
        
        for i in range(n):
            for j in range(size-1, -1, -1):
                res.append(res[j] | 1 << i)
                size += 1
        return res
            
```

## refs

* [lc](https://leetcode.com/problems/gray-code/)


