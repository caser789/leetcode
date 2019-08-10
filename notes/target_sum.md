---
tags: [2019/08/10, leetcode/494, method/traversal/dfs]
title: Target Sum
created: '2019-08-10T08:25:09.770Z'
modified: '2019-08-10T08:46:05.107Z'
---

# Target Sum


You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

### Example 1:

```
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
```

There are 5 ways to assign symbols to make the sum of nums be target 3.

> The length of the given array is positive and will not exceed 20.
> The sum of elements in the given array will not exceed 1000.
> Your output answer is guaranteed to be fitted in a 32-bit integer.

## Solution

### TLE

```python
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        >>> nums = [1, 1, 1, 1, 1]
        >>> S = 3
        >>> Solution().findTargetSumWays(nums, S)
        5
        >>> nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        >>> S = 1
        >>> Solution().findTargetSumWays(nums, S)
        32768
        >>> nums = [1, 0]
        >>> S = 1
        >>> Solution().findTargetSumWays(nums, S)
        2
        """
        count_of_0 = sum(1 for num in nums if not num)
        nums = [num for num in nums if num]
        combine = tuple(1 for num in nums)
        stack = [combine]
        cnt = 0

        seen = set()
        seen.add(combine)
        while stack:
            combine = stack.pop()
            if self.sum(combine, nums) == S:
                cnt += 1
            for nei in self.neighbours(combine):
                if nei in seen: continue
                stack.append(nei)
                seen.add(nei)
        return cnt * (2**count_of_0)

    def neighbours(self, combine):
        for i, c in enumerate(combine):
            yield combine[:i] + (-1*c,) + combine[i+1:]

    def sum(self, combine, nums):
        return sum(i*j for i, j in zip(combine, nums))
```
