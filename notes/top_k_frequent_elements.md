---
tags: [2019/08/19, data structure/map, data structure/priority queue, leetcode/347, method/search/search, method/sort]
title: Top K Frequent Elements
created: '2019-08-01T05:46:51.151Z'
modified: '2019-08-19T13:25:01.499Z'
---

# Top K Frequent Elements


Given a non-empty array of integers, return the k most frequent elements.

### Example 1:

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

### Example 2:

```
Input: nums = [1], k = 1
Output: [1]
```

> You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
> Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


## Solution

```python
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        >>> nums = [1, 1, 1, 2, 2, 3]
        >>> k = 2
        >>> Solution().topKFrequent(nums, k)
        [1, 2]
        >>> nums = [1]
        >>> k = 1
        >>> Solution().topKFrequent(nums, k)
        [1]
        """
        store = {}
        for num in nums:
            store.setdefault(num, 0)
            store[num] += 1

        items = store.items()
        items.sort(key=lambda x: -x[1])
        return [items[i][0] for i in range(k)]
```
