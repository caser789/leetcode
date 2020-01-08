---
tags: [2019/12/21, application/array/prefix-sum, application/matrix/kth, data structure/queue, leetcode/719, method/search/binary, TODO]
title: Find K-th Smallest Pair Distance
created: '2019-10-19T08:27:09.149Z'
modified: '2019-12-18T15:49:58.393Z'
---

# Find K-th Smallest Pair Distance

Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.

### Note:

2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.

## solution


### sort

```
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        diffs = list()
        for i in range(1, len(nums)):
            d = nums[i] - nums[i-1]
            diffs.append(d)

        diffs.sort()
        return diffs[k-1]
```


### heap1

```python
import heapq
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        pq = [(nums[i+1]-nums[i], i, i+1) for i in range(n-1)]
        heapq.heapify(pq)

        for _ in range(k):
            d, root, nei = heapq.heappop(pq)
            if nei + 1 < n:
                heapq.heappush(pq, (nums[nei+1]-nums[root], root, nei+1))

        return d

```

### heap TLE

```
import heapq


class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        1 1 3

        """
        nums.sort()
        n = len(nums)
        pq = []

        for i in range(n):
            for j in range(i+1, n):
                d = nums[j] - nums[i]
                heapq.heappush(pq, -d)
                if len(pq) > k:
                    heapq.heappop(pq)

        return -pq[0]



```


### binary search + prefix sum

```python
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        w = nums[-1]

        # multiplicity[i] = number of nums[j] == nums[i] (j < i)
        multiplicity = [0] * n
        for i, x in enumerate(nums):
            if i and x == nums[i-1]:
                multiplicity[i] = 1 + multiplicity[i-1]

        # prefix[v] = number of values <= v
        prefix = [0] * (w+1)
        left = 0
        for i in range(len(prefix)):
            while left < len(nums) and nums[left] == i:
                left += 1
            prefix[i] = left

        def possible(d):
            # is there k or more pairs with dist <= d?
            return sum(
                prefix[min(x + d, w)] - prefix[x] + multiplicity[i]
                for i, x in enumerate(nums)
            ) >= k

        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi)/2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo
```

### binary search + binary search

```python
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)

        def search(val, i, j):
            while i < j:
                mi = (i+j)/2
                if nums[mi] <= val:
                    i = mi + 1
                else:
                    j = mi
            return i

        def count(val):
            c = 0
            for i in range(n):
                j = search(val+nums[i], i+1, n)
                c += j - i - 1
            return c

        lo = 0
        hi = nums[n-1] - nums[0]
        while lo < hi:
            mi = (lo+hi)/2
            if count(mi) >= k:
                hi = mi
            else:
                lo = mi + 1

        return lo
```

## schedule

* [x] 2019/10/19
* [x] 2019/12/16
* [x] 2019/12/18
* [ ] 2019/12/21

