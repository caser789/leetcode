---
tags: [2019/10/20, data structure/queue, leetcode/719, TODO]
title: Find K-th Smallest Pair Distance
created: '2019-10-19T08:27:09.149Z'
modified: '2019-10-19T09:14:34.241Z'
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
Note:
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

## schedule

* [x] 2019/10/19
* [ ] 2019/10/20

