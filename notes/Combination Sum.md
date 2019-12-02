---
tags: [2019/11/08, application/combination, leetcode/39, method/backtrack]
title: Combination Sum
created: '2019-11-08T05:24:17.769Z'
modified: '2019-11-23T09:50:30.324Z'
---

# Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

## Solution

```python
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        f(3, 7) = f(2, 7) + f(2, 7-7) + 7
        Input: candidates = [2,3,6,7], target = 7,
        A solution set is:
        [
            [7],
            [2,2,3]
        ]
        """

        def find(i, s, res, tmp):
            if i < 0:
                return

            find(i-1, s, res, tmp[:])

            if s == candidates[i]:
                tmp.append(s)
                res.append(tmp)
            elif s > candidates[i]:
                tmp.append(candidates[i])
                find(i, s-candidates[i], res, tmp)

        res = []
        tmp = []
        find(len(candidates)-1, target, res, tmp)
        return res



```


## refs

* [lc](https://leetcode.com/problems/combination-sum/)
* [backtrack](https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning))
