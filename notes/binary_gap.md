---
tags: [2019/09/26, leetcode/868]
title: Binary Gap
created: '2019-09-22T11:23:17.129Z'
modified: '2019-09-24T14:08:16.413Z'
---

# Binary Gap

Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.

 

### Example 1:

Input: 22
Output: 2
Explanation: 
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.

### Example 2:

Input: 5
Output: 2
Explanation: 
5 in binary is 0b101.

### Example 3:

Input: 6
Output: 1
Explanation: 
6 in binary is 0b110.

### Example 4:

Input: 8
Output: 0
Explanation: 
8 in binary is 0b1000.

There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.
 

## Note:

1 <= N <= 10^9

## Solution

```python
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        digits = []
        while N:
            N, c = divmod(N, 2)
            digits.append(c)

        n = len(digits)
        i = 0
        while i < n and digits[i] == 0:
            i += 1

        if i == n:
            return 0

        cnt = 0
        res = []
        cnt_one = 0
        while i < n:
            if digits[i] == 1:
                res.append(cnt)
                cnt = 0
                cnt_one += 1
            else:
                cnt += 1
            i += 1
        if not res: return 0
        if cnt_one < 2: return 0
        return max(res)+1


print Solution().binaryGap(5)
print Solution().binaryGap(6)
print Solution().binaryGap(8)
    
```

### shift

```python
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        A = [i for i in range(32) if (N>>i) & 1]
        if len(A) < 2:
            return 0
        return max(A[i+1] - A[i] for i in range(len(A)-1))
```

### one-pass

```python
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        last = None
        res = 0
        for i in range(32):
            if (N >> i) & 1:
                if last is not None:
                    res = max(res, i - last)
                last = i
        return res
```

## schedule

* [x] 0 2019/09/25
* [ ] 1 2019/09/26
