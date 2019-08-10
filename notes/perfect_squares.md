---
title: Perfect Squares
created: '2019-08-05T05:56:38.797Z'
modified: '2019-08-05T05:56:52.569Z'
---

# Perfect Squares


Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

### Example 1:

```
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
```

### Example 2:

```
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```

## Solution

```python
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0

        if n == 1:
            return 1
        squares = [i*i for i in range(n, 0, -1) if i*i <= n]
        if n in squares:
            return 1

        cnt = 0
        q = [0]

        while q:
            cnt += 1
            nxt_q = []
            for node in q:
                for nei in self.neighbours(node, squares):
                    if nei == n:
                        return cnt
                    nxt_q.append(nei)
            q = nxt_q
        return 0

    def neighbours(self, num, squares):
        for square in squares:
            yield num + square

assert Solution().numSquares(1) == 1
assert Solution().numSquares(2) == 2
assert Solution().numSquares(3) == 3
assert Solution().numSquares(4) == 1
assert Solution().numSquares(13) == 2
assert Solution().numSquares(12) == 3
print Solution().numSquares(36)
```
