---
tags: [2019/08/17, leetcode/746, method/dp]
title: Min Cost Climbing Stairs
created: '2019-08-17T09:18:47.079Z'
modified: '2019-08-17T09:19:25.702Z'
---

# Min Cost Climbing Stairs

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

### Example 1:

```
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
```

### Example 2:

```
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
```

> cost will have a length in the range [2, 1000].
> Every cost[i] will be an integer in the range [0, 999].

## Solution

```python
class Solution(object):
    def minCostClimbingStairs(self, costs):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(costs)
        return self._dp(costs, n)

    def _dp(self, costs, i):
        if i == 1:
            return 0
        dp = [0] * (i+1)
        dp[1] = 0
        for j in range(2, i+1):
            dp[j] = min(dp[j-1] + costs[j-1], dp[j-2] + costs[j-2])
        return dp[i]
```
