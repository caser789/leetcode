---
tags: [2019/08/29, leetcode/1128, TODO]
title: Number of Equivalent Domino Pairs
created: '2019-08-29T14:48:00.633Z'
modified: '2019-08-29T14:59:20.330Z'
---

# Number of Equivalent Domino Pairs

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

### Example 1:

```
Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
```


> 1 <= dominoes.length <= 40000
> 1 <= dominoes[i][j] <= 9

## Solution

```python
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
```
