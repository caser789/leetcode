---
tags: [2019/11/22, leetcode/1262]
title: Greatest Sum Divisible by Three
created: '2019-11-22T05:17:54.601Z'
modified: '2019-11-22T05:31:34.221Z'
---

# Greatest Sum Divisible by Three

Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.

 

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 

Constraints:

1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4

## Solution

### backtrack

```python
class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        f(i, s) = max(f(i-1, s-ss) + f(i-1, s))
        """
        
        s = sum(nums)
        if s % 3 == 0:
            return s
        
        n = len(nums)
        
        self.max = 0
        
        def collect(seen, s):
            if s % 3 == 0:
                self.max = max(self.max, s)
            
            for i in range(n):
                if i in seen: continue
                    
                s += nums[i]
                seen.add(i)
                
                collect(seen, s)
                
                seen.remove(i)
                s -= nums[i]
        
        collect(set(), 0)
        return self.max
                
            
```

### dp bottom up

```python
class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Input: nums = [3,6,5,1,8]
        1 3 5 6 8

        23 % 3 == 2
        Output: 18 = 1 3 6 8 
        """
        seen = [0, 0, 0]
        for num in nums:
            for s in seen[:]:
                j = (s+num)%3
                seen[j] = max(seen[j], s+num)
        return seen[0]

```

## refs

* [lc](https://leetcode.com/problems/greatest-sum-divisible-by-three/)
* [diss](https://leetcode.com/problems/greatest-sum-divisible-by-three/discuss/431077/JavaC%2B%2BPython-One-Pass-O(1)-space)


