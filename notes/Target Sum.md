---
tags: [2019/11/04, leetcode/494]
title: Target Sum
created: '2019-11-03T08:29:04.235Z'
modified: '2019-11-03T10:06:19.988Z'
---

# Target Sum

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.

## Solution

### brute force

```python
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.count = 0
        self.calculate(nums, 0, 0, S)
        return self.count
    
    def calculate(self, nums, i, s, S):
        if i == len(nums):
            if s == S:
                self.count += 1
        else:
            self.calculate(nums, i+1, s+nums[i], S)
            self.calculate(nums, i+1, s-nums[i], S)
```

### top-down dp

```python
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.count = 0
        n = len(nums)
        memo = [[-float('inf')] * 2001 for _ in range(n)]
        
        return self.calculate(nums, 0, 0, S, memo)
    
    def calculate(self, nums, i, s, S, memo):
        if i == len(nums):
            if s == S:
                return 1
            return 0
        
        if memo[i][s+1000] != -float('inf'):
            return memo[i][s+1000]
        
        x = self.calculate(nums, i+1, s+nums[i], S, memo)
        y = self.calculate(nums, i+1, s-nums[i], S, memo)
        memo[i][s+1000] = x + y
        return memo[i][s+1000]
        
        
        
```

### top-down dp 2

```python
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        
        n = len(nums)
        d = {}
        return self.collect(nums, n-1, S, d)
        
    
    def collect(self, nums, i, s, d):
        if i < 0:
            if s == 0:
                return 1
            return 0
        

        
        if (i, s) in d:
            return d[(i, s)]
        
        x = self.collect(nums, i-1, s+nums[i], d)
        y = self.collect(nums, i-1, s-nums[i], d)
        d[(i, s)] = x + y
        return d[(i, s)]
            
            
```

### buttom-up

```python
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)
        dp = [[0]*2001 for _ in range(n)]
        dp[0][nums[0]+1000] = 1
        dp[0][-nums[0]+1000] += 1
        for i in range(1, n):
            for s in range(-1000, 1001):
                if dp[i-1][s+1000] > 0:
                    dp[i][s+nums[i]+1000] += dp[i-1][s+1000]
                    dp[i][s-nums[i]+1000] += dp[i-1][s+1000]
        
        return 0 if S > 1000 else dp[n-1][S+1000]
```

### 1D DP

```python
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)
        dp = [0] * 2001
        dp[nums[0]+1000] += 1
        dp[-nums[0]+1000] += 1
        
        for i in range(1, n):
            nxt = [0] * 2001
            for s in range(-1000, 1001):
                if dp[s+1000] > 0:
                    nxt[s+nums[i]+1000] += dp[s+1000]
                    nxt[s-nums[i]+1000] += dp[s+1000]
            dp = nxt
        
        return 0 if S > 1000 else dp[S+1000]
```

## schedule

* [x] 2019/11/03
* [ ] 2019/11/04

## refs

* [lc](https://leetcode.com/problems/target-sum/)
