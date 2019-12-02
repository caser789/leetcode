---
tags: [2019/11/06, leetcode/377]
title: Combination Sum IV
created: '2019-11-06T00:21:04.291Z'
modified: '2019-11-06T00:29:11.619Z'
---

# Combination Sum IV

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
 

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

## Solution

### brute force

```python
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        f(4) = f(3) + f(2) + f(1)
        f(1) = f(0) + f(-1) + f(-2)
        f(2) = f(1) + f(0) + f(-1)
        """
        if target < 0:
            return 0
        if target == 0:
            return 1
        
        res = 0
        for num in nums:
            i = self.combinationSum4(nums, target-num)
            res += i
        
        return res
```

### DP top-down

```python
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        f(4) = f(3) + f(2) + f(1)
        f(1) = f(0) + f(-1) + f(-2)
        f(2) = f(1) + f(0) + f(-1)
        """
        cache = {}
        def find(amt):
            
            if amt < 0:
                return 0
            if amt == 0:
                return 1
            if amt in cache:
                return cache[amt]

            res = 0
            for num in nums:
                i = find(amt-num)
                res += i
            
            cache[amt] = res
            return res
        
        return find(target)
```

### DP bottom-up

```python
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        f(4) = f(3) + f(2) + f(1)
        f(1) = f(0) + f(-1) + f(-2)
        f(2) = f(1) + f(0) + f(-1)
        """
        if target < 0:
            return 0
        if target == 0:
            return 1
        
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, target+1):
            cnt = 0
            for num in nums:
                if i - num >= 0:
                    cnt += dp[i-num]
            dp[i] = cnt
        
        return dp[target]
```

## schedule

* [x] 2019/11/06
* [ ] 2019/11/07

## refs

* [lc](https://leetcode.com/problems/combination-sum-iv/)

