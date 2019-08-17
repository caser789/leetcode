---
tags: [2019/08/17, leetcode/877, method/dp, TODO]
title: Stone Game
created: '2019-08-17T10:44:00.806Z'
modified: '2019-08-17T11:01:14.954Z'
---

# Stone Game

Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

### Example 1:

```
Input: [5,3,4,5]
Output: true
Explanation:
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
```


> 2 <= piles.length <= 500
> piles.length is even.
> 1 <= piles[i] <= 500
> sum(piles) is odd.

## Solution

### custom

```python
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        m = n / 2
        alex = [0] * (m+1)
        lee = [0] * (m+1)
        lo = 0
        hi = n - 1
        for i in range(1, m+1):
            if piles[lo] > piles[hi]:
                alex[i] = piles[lo]
                lo += 1
            else:
                alex[i] = piles[hi]
                hi -= 1

            if piles[lo] > piles[hi]:
                lee[i] = piles[lo]
                lo += 1
            else:
                alex[i] = piles[hi]
                hi -= 1

            i += 1
        return alex[m] > lee[m]
```

### custom

```python
class Solution(object):
    def _stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        m = n / 2
        alex = [0] * (m+1)
        lee = [0] * (m+1)
        lo = 0
        hi = n - 1
        for i in range(1, m+1):
            if piles[lo] > piles[hi]:
                alex[i] = piles[lo]
                lo += 1
            else:
                alex[i] = piles[hi]
                hi -= 1

            if piles[lo] > piles[hi]:
                lee[i] = piles[lo]
                lo += 1
            else:
                alex[i] = piles[hi]
                hi -= 1

            i += 1
        return alex[m] > lee[m]

    def stoneGame(self, piles):
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for lo in range(n):
            dp[lo][lo] = piles[lo]
        for j in range(1, n):
            # i + j < n
            for i in range(n-j):
                dp[i][i+j] = max(piles[i]- dp[i+1][i+j], piles[i+j] - dp[i][i+j-1])
        return dp[0][-1] > 0
```
