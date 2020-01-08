---
tags: [2019/12/07, leetcode/209, method/sliding-window]
title: Minimum Size Subarray Sum
created: '2019-12-07T06:31:23.025Z'
modified: '2019-12-08T05:48:56.345Z'
---

# Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 


## Solution

```python
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = n + 1
        i = 0
        for j in range(n):
            s -= nums[j]
            while s <= 0:
                res = min(res, j-i+1)
                s += nums[i]
                i += 1
        
        
        return res % (n+1)

```

### O(n**3)

```python
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = n + 1
        for i in range(n):
            for j in range(i, n):
                sum = 0
                for k in range(i, j+1):
                    sum += nums[k]
                if sum >= s:
                    res = min(res, j-i+1)
                    break
                    
        
        return res % (n+1)
```

### O(n**2)

```python
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        
        res = n + 1
        sums = [0] * n
        sums[0] = nums[0]
        for i in range(1, n):
            sums[i] = nums[i] + sums[i-1]
        
        for i in range(n):
            for j in range(i, n):
                sum = sums[j] - sums[i] + nums[i]
                if sum >= s:
                    res = min(res, j - i + 1)
                    break
                    
        return res % (n+1)
```

### nlg(n) binary search

```python
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        
        res = n + 1
        sums = [0] * n
        sums[0] = nums[0]
        
        for i in range(1, n):
            sums[i] = sums[i-1] + nums[i]
        
        for i in range(n):
            A = s + sums[i] - nums[i]
            j = find(sums, A, n)
            if sums[j] == A:
                res = min(res, j - i + 1)
            elif j + 1 < n:
                res = min(res, j + 1 - i + 1)
        
        return res % (n+1)
            
            

def find(nums, target, n):
    i = 0
    j = n - 1
    
    while i <= j:
        mi = (i+j) / 2
        if nums[mi] == target:
            return mi
        if target < nums[mi]:
            j -= 1
        else:
            i += 1
    return j

        
        
            
```

## refs

* [lc](https://leetcode.com/problems/minimum-size-subarray-sum/)
* [sliding window](https://leetcode.com/problems/minimum-size-subarray-sum/discuss/433123/JavaC%2B%2BPython-Sliding-Window)
* [solution](https://leetcode.com/problems/minimum-size-subarray-sum/solution/)
