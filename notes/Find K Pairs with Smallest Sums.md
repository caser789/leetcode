---
tags: [2019/12/23, application/matrix/kth, data structure/priority queue, leetcode/373]
title: Find K Pairs with Smallest Sums
created: '2019-10-19T07:05:21.857Z'
modified: '2019-12-22T11:34:43.897Z'
---

# Find K Pairs with Smallest Sums

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]


## Solution

### sort

```python
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        n = len(nums1)
        m = len(nums2)
        res = []
        for i in range(n):
            for j in range(m):
                s = nums1[i] + nums2[j]
                res.append((s, i, j))
        
        res.sort()
        
        return [[nums1[res[i][1]], nums2[res[i][2]]] for i in range(min(k, n*m))]
```

### pq1

```python
import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        
        n = len(nums1)
        m = len(nums2)
        pq = []
        for i in range(n):
            for j in range(m):
                v = nums1[i] + nums2[j]
                heapq.heappush(pq, (-v, nums1[i], nums2[j]))
                
                if len(pq) > k:
                    heapq.heappop(pq)
        res = []
        for i in range(len(pq)):
            v, a, b = heapq.heappop(pq)
            res.append([a, b])
        return res
```

### better pq

```python
import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        n = len(nums1)
        m = len(nums2)
        pq = []
        for i in range(n):
            s = nums1[i] + nums2[0]
            heapq.heappush(pq, (s, i, 0))
        
        res = []
        while k and pq:
            s, i, j = heapq.heappop(pq)
            res.append([nums1[i], nums2[j]])
            k -= 1
            if j + 1 < m:
                j += 1
                s = nums1[i] + nums2[j]
                heapq.heappush(pq, (s, i, j))
        
        return res
```

## refs

* [378](https://leetcode.com/problems/k-th-smallest-prime-fraction/discuss/115819/Summary-of-solutions-for-problems-%22reducible%22-to-LeetCode-378)
* [lc](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

## schedule

* [x] 2019/10/19
* [x] 2019/10/20
* [x] 2019/10/25
* [x] 2019/12/22
* [ ] 2019/12/23
