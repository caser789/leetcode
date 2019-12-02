---
tags: [2019/11/17, application/split-array, leetcode/842, method/backtrack]
title: Split Array into Fibonacci Sequence
created: '2019-11-17T02:30:58.079Z'
modified: '2019-11-25T10:11:04.025Z'
---

# Split Array into Fibonacci Sequence

Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]
Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]
Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.
Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.

## Note:

1 <= S.length <= 200
S contains only digits.

## Solution

```python
class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(S)
        if n < 3:
            return []

        res = []
        def collect(i, tmp):
        
            if len(tmp) > 2:
                if tmp[-1] != tmp[-2] + tmp[-3]:
                    return
            if i == n:
                if len(tmp) > 2:
                    res.append(tmp[:])
                return
            for j in range(i+1, n+1):  
                if S[i] == '0' and j > i+1: continue
                w = S[i:j]
                w = int(w)
                if not 0 <= w <= 2**31-1: continue
                tmp.append(w)  
                collect(j, tmp)    
                tmp.pop()
        
        collect(0, [])
        return res[0] if res else res
```

### backtrack 2

```python
class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(S)
        res = []
        tmp = []

        def search(i):
            if len(tmp) > 2 and tmp[-1] != tmp[-2] + tmp[-3]:
                return

            if i == n:
                if len(tmp) > 2:
                    res.append(tmp[:])
                return

            for j in range(i, n):
                if j > i and S[i] == '0': return
                w = S[i:j+1]
                w = int(w)
                if w > 2**31 - 1: return

                tmp.append(w)
                search(j+1)
                tmp.pop()


        search(0)
        return res[0] if res else res


```

### backtrack 3

```python
class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(S)
        res = []
        tmp = []

        def search(i):
            if len(tmp) > 2 and tmp[-1] != tmp[-2] + tmp[-3]:
                return False

            if i == n:
                if len(tmp) > 2:
                    res.append(tmp[:])
                    return True
                return False

            for j in range(i, n):
                if j > i and S[i] == '0': return False
                w = S[i:j+1]
                w = int(w)
                if w > 2**31 - 1: return False

                tmp.append(w)
                if search(j+1): return True
                tmp.pop()
            return False


        search(0)
        return res[0] if res else res

```

## refs

* [lc](https://leetcode.com/problems/split-array-into-fibonacci-sequence/)
