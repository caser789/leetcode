---
favorited: true
tags: [2019/12/31, data structure/set, leetcode/128, method/union find]
title: Longest Consecutive Sequence
created: '2019-10-31T14:43:39.242Z'
modified: '2019-12-30T14:21:03.824Z'
---

# Longest Consecutive Sequence


Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

## Solution

### brute force

```python
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_streak = 0
        for num in nums:
            current_num = num
            current_streak = 1
            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1
            
            longest_streak = max(longest_streak, current_streak)
        return longest_streak
```

### sort

```python
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return n
        
        nums.sort()
        longest = 1
        cur = 1
        
        for i in range(1, n):
            if nums[i] == nums[i-1] + 1:
                cur += 1
            elif nums[i] != nums[i-1]:
                longest = max(longest, cur)
                cur = 1
        
        return max(longest, cur)             
```

### set

```python
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_streak = 0
        num_set = set(nums)
        
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
        return longest_streak
```

### UF

```python
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return n
        
        uf = UF(n)
        kv = {}
        for i, num in enumerate(nums):
            if num in kv: continue
            kv[num] = i
            
            if num - 1 in kv:
                uf.union(i, kv[num-1])
            
            if num + 1 in kv:
                uf.union(i, kv[num+1])
        
        return uf.max()
        
        
        
class UF(object):
    
    def __init__(self, n):
        self.n = n
        self.parents = range(n)
        self.size = [0] * n
    
    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return
        
        if self.size[rootp] < self.size[rootq]:
            self.parents[rootp] = rootq
        elif self.size[rootp] > self.size[rootq]:
            self.parents[rootq] = rootp
        else:
            self.size[rootq] += 1
            self.parents[rootp] = rootq
        
    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p
    
    def max(self):
        lst = [0] * self.n
        for i in range(self.n):
            root = self.find(i)
            lst[root] += 1
        return max(lst)

```

## schedule

* [x] 2019/10/31
* [x] 2019/12/30
* [ ] 2019/12/31

## refs

* [lc](https://leetcode.com/problems/longest-consecutive-sequence/)

