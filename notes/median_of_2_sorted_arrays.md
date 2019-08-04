---
title: Median of Two Sorted Arrays
created: '2019-08-04T04:12:16.842Z'
modified: '2019-08-04T04:12:35.658Z'
---

# Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

### Example 1:

```
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```

### Example 2:

```
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```

## Solution

```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        >>> nums1 = [1, 3]
        >>> nums2 = [2]
        >>> Solution().findMedianSortedArrays(nums1, nums2)
        2.0
        >>> nums1 = [1, 2]
        >>> nums2 = [3, 4]
        >>> Solution().findMedianSortedArrays(nums1, nums2)
        2.5
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 , m, n = nums2, nums1, n, m

        imin, imax, half_length = 0, m, (m+n+1)/2
        while imin <= imax:
            i = (imin+imax)/2
            j = half_length - i
            # i too small
            if i < m and nums1[i] < nums2[j-1]:
                imin = i + 1
            # i too large
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            # i is perfect
            else:
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])

                if (m+n)%2:
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left+min_of_right)/2.0
```
