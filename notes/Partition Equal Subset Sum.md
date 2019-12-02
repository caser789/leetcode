---
tags: [2019/11/04, leetcode/416]
title: Partition Equal Subset Sum
created: '2019-11-04T14:53:31.304Z'
modified: '2019-11-05T13:44:11.227Z'
---

# Partition Equal Subset Sum

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

## Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

### Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

### Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

## Solution

### brute force

```python
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        f(i, s) = f(i-1, s) or f(i-1, s-nums[i])
        """
        s = sum(nums)
        
        if s & 1:
            return False
        
        half = s / 2
        return find(nums, len(nums)-1, half)
        

def find(nums, i, s):
    if s <= 0:
        return False
    
    if i == 0:
        if s == nums[0]:
            return True
        return False
    
    x = find(nums, i-1, s)
    y = find(nums, i-1, s-nums[i])
    return x or y
        
        
```

### dp top-down

```python
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        f(i, s) = f(i-1, s) or f(i-1, s-nums[i])
        """
        s = sum(nums)

        if s & 1:
            return False

        half = s / 2
        d = {}
        return find(nums, len(nums)-1, half, d)


def find(nums, i, s, d):
    if (i, s) in d:
        return d[(i, s)]

    if s <= 0:
        return False

    if i == 0:
        if s == nums[0]:
            return True
        return False

    x = find(nums, i-1, s, d)
    if x:
        d[(i, s)] = True
        return d[(i, s)]

    y = find(nums, i-1, s-nums[i], d)
    d[(i, s)] = True if y else False
    return d[(i, s)]

```

### dp bottom-up

```python
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        f(i, s) = f(i-1, s) or f(i-1, s-nums[i])
        """
        s = sum(nums)

        if s & 1:
            return False

        n = len(nums)
        half = s / 2
        dp = [[False] * (half+1) for _ in range(n+1)]
        
        dp[0][0] = True
        for i in range(1, n+1):
            dp[i][0] = True
        
        for i in range(1, half+1):
            dp[0][i] = False
        
        for i in range(1, n+1):
            for j in range(1, half+1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i-1]:
                    dp[i][j] |= dp[i-1][j-nums[i-1]]
        return dp[n][half]


```

### 1D DP

```python
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        """
        
        n = len(nums)
        s = sum(nums)
        if s & 1:
            return False
        
        s = s / 2
        
        prev = [False] * (s+1)
        j = nums[0]
        if j <= s:
            prev[j] = True
        
        for i in range(1, n):
            nxt = [False] * (s+1)
            for j in range(s+1):
                nxt[j] = prev[j]
                if j - nums[i] >= 0:
                    
                    nxt[j] |= prev[j-nums[i]]
            prev = nxt
        
        
        return prev[-1]
```
