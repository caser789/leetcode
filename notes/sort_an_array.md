---
tags: [2019/08/15, leetcode/912, method/devide and conquer, method/sort]
title: Sort an Array
created: '2019-08-15T14:32:55.754Z'
modified: '2019-08-26T15:02:00.271Z'
---

# Sort an Array


Given an array of integers nums, sort the array in ascending order.



### Example 1:

```
Input: [5,2,3,1]
Output: [1,2,3,5]
```

### Example 2:

```
Input: [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
```



> 1 <= A.length <= 10000
> -50000 <= A[i] <= 50000


## Solution

```python
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.merge_sort(nums)
        return nums

    def merge_sort(self, nums):
        n = len(nums)
        if n <= 1:
            return

        mid = n / 2
        left = nums[:mid]
        right = nums[mid:]
        self.merge_sort(left)
        self.merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
```
