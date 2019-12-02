---
tags: [2019/10/28, data structure/monoqueue, leetcode/503]
title: Next Greater Element II
created: '2019-10-27T11:58:17.032Z'
modified: '2019-11-21T13:59:40.671Z'
---

# Next Greater Element II

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

### Example 1:
Input: [1,2,1]
Output: [2,-1,2]

Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.

## Note: The length of given array won't exceed 10000.

## Solution



### brute force

```python
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        dnums = nums * 2
        for i in range(n):
            for j in range(i+1, n*2):
                if dnums[j] > dnums[i]:
                    res[i] = dnums[j]
                    break
        return res
        
```

### better brute force

```python
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        for i in range(n):
            for j in range(1, n):
                if nums[(i+j)%n] > nums[i]:
                    res[i] = nums[(i+j)%n]
                    break
        return res
```

### stack

```python
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(n*2):
            num = nums[i%n]
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
            
            if i < n:
                stack.append(i)
        return res
```

## schedule

* [x] 2019/10/27
* [ ] 2019/10/28
