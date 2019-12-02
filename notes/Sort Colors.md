---
tags: [2019/11/05, leetcode/75, method/sort/quick/3]
title: Sort Colors
created: '2019-11-05T01:17:54.396Z'
modified: '2019-11-05T01:26:30.134Z'
---

# Sort Colors

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

## Solution

### brute force

```python
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        counter = [0] * 3
        for num in nums:
            counter[num] += 1
        
        i = 0
        for _ in range(counter[0]):
            nums[i] = 0
            i += 1
        
        for _ in range(counter[1]):
            nums[i] = 1
            i += 1
        
        for _ in range(counter[2]):
            nums[i] = 2
            i += 1
        
        
```

### partition 3

```python
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero = -1
        i = 0
        two = n
        
        while i < two:
            if nums[i] == 0:
                zero += 1
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                two -= 1
                nums[two], nums[i] = nums[i], nums[two]
```

## schedule

* [x] 2019/11/05
* [ ] 2019/11/06

## refs

* [lc](https://leetcode.com/problems/sort-colors/)
* [liwei](https://www.liwei.party/2018/10/16/leetcode-solution/array3/#toc-heading-3)
