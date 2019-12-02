---
tags: [2019/10/31, leetcode/238, method/direction]
title: Product of Array Except Self
created: '2019-09-04T14:35:39.784Z'
modified: '2019-11-09T13:59:24.940Z'
---

# Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

### Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

> Note: Please solve it without division and in O(n).

## Follow up:

Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

## Solution

### brute force

```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        for i in range(n):
            p = 1
            for j in range(n):
                if j == i: continue
                p *= nums[j]
            res.append(p)
        return res
            
```

### with division

```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        p = 1
        find = False
        for num in nums:
            if num == 0:
                if find:                    
                    for i in range(n):
                        nums[i] = 0
                    return nums
                else:
                    find = True
                    continue
            p *= num
        
        
        for i in range(n):
            if nums[i] != 0:
                if find:
                    nums[i] = 0
                else:
                    nums[i] = p / nums[i]
            else:
                nums[i] = p
        
        return nums
        
        
                    
            
```

### left and right list

```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        s = 1
        left = [1] * n
        for i in range(n-1):
            s *= nums[i]
            left[i+1] = s

        s = 1
        right = [1] * n
        for i in range(n-1, 0, -1):
            s *= nums[i]
            right[i-1] = s

        for i in range(n):
            nums[i] = left[i] * right[i]
        return nums
```

### O(n)

```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n
        
        res[0] = 1
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        
        r = 1
        for i in range(n-1, -1, -1):
            res[i] *= r
            r *= nums[i]
        
        return res
            
```

## schedule

* [x] 0 2019/09/04
* [x] 1 2019/09/05
* [x] 1 2019/09/08
* [x] 1 2019/09/15
* [x] 1 2019/09/30
* [ ] 1 2019/10/31
