---
tags: [2019/11/21, application/divmod, leetcode/1009]
title: Complement of Base 10 Integer
created: '2019-09-22T11:22:09.307Z'
modified: '2019-10-22T15:17:35.677Z'
---

# Complement of Base 10 Integer

Every non-negative integer N has a binary representation.  For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in binary is "010" in binary.

For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.

 

Example 1:

Input: 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
Example 2:

Input: 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
Example 3:

Input: 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
 

Note:

0 <= N < 10^9

## Solution

```python
class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 1
        
        res = []
        while N:
            N, c = divmod(N, 2)
            res.append(c)
        m = 0
        for c in res[::-1]:
            v = 1 if c == 0 else 0
            m = m * 2 + v
        return m
                
```

## schedule

* [x] 0 2019/09/25
* [x] 1 2019/09/26
* [x] 1 2019/09/29
* [x] 1 2019/10/06
* [x] 1 2019/10/21
* [ ] 1 2019/11/21
