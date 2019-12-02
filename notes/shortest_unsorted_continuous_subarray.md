---
favorited: true
tags: [2019/11/26, data structure/monoqueue, data structure/stack, leetcode/581]
title: Shortest Unsorted Continuous Subarray
created: '2019-08-31T08:34:12.401Z'
modified: '2019-10-27T11:57:12.850Z'
---

# Shortest Unsorted Continuous Subarray

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

### Example 1:

Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

> Then length of the input array is in range [1, 10,000].
> The input array may contain duplicates, so ascending order here means <=.


## Solution

### sort

```python
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = sorted(nums)
        n = len(x)
        i = 0
        while i < n and x[i] == nums[i]:
            i += 1
        j = n - 1
        while j >= 0 and x[j] == nums[j]:
            j -= 1
        
        res = j - i + 1
        return res if res >= 0 else 0
            
```

### stack

```python
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        n = len(nums)
        l = n
        r = 0
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)
            
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                r = max(r, stack.pop())
            stack.append(i)
        
        return r - l + 1 if r - l + 1 >= 0 else 0
```

## schedule

* [x] 0 2019/09/30
* [x] 1 2019/10/01
* [x] 1 2019/10/04
* [x] 1 2019/10/11
* [x] 1 2019/10/26
* [ ] 1 2019/11/26
