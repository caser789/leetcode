---
deleted: true
tags: [2019/10/14, leetcode/857]
title: Minimum Cost to Hire K Workers
created: '2019-10-13T11:24:34.585Z'
modified: '2019-10-14T13:50:54.827Z'
---

# Minimum Cost to Hire K Workers

There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above conditions.

 

### Example 1:

Input: quality = [10,20,5], wage = [70,50,30], K = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.

### Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
Output: 30.66667
Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately. 
 

## Note:

1 <= K <= N <= 10000, where N = quality.length = wage.length
1 <= quality[i] <= 10000
1 <= wage[i] <= 10000
Answers within 10^-5 of the correct answer will be considered correct.

## Solution

### intuitive

```python
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        from fractions import Fraction
        res = float('inf')
        
        n = len(quality)
        for i in range(n):
            factor = Fraction(wage[i], quality[i])
            prices = []
            for w in range(n):
                price = factor * quality[w]
                if price < wage[w]: continue
                prices.append(price)
            if len(prices) < K:
                continue
            prices.sort()
            res = min(res, sum(prices[:K]))
        return float(res)
```
