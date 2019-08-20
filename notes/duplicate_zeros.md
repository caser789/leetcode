---
tags: [2019/08/20, leetcode/1089]
title: Duplicate Zeros
created: '2019-08-20T12:51:12.191Z'
modified: '2019-08-20T12:51:36.504Z'
---

# Duplicate Zeros


Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.


### Example 1:

```
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
```

### Example 2:

```
Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
```


> 1 <= arr.length <= 10000
> 0 <= arr[i] <= 9


## Solution

```python
class Solution(object):
    def duplicateZeros(self, nums):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        cnt = 0
        for num in nums:
            if num == 0:
                cnt += 1

        n = len(nums)
        cnt += n
        i = n - 1
        j = cnt - 1
        while i < j:
            if nums[i] == 0:
                if j < n:
                    nums[j] = 0
                j -= 1
                if j < n:
                    nums[j] = 0
            else:
                if j < n:
                    nums[j] = nums[i]
            i -= 1
            j -= 1
```
