---
tags: [2019/12/22, data structure/monoqueue, leetcode/239]
title: Sliding Window Maximum
created: '2019-10-22T04:47:02.715Z'
modified: '2020-01-07T13:44:21.392Z'
---

# Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?

## Solution

```python
from collections import deque


class Monoqueue(object):

    def __init__(self):
        self.queue = deque()

    def push(self, val):
        cnt = 0
        while len(self.queue) > 0 and self.queue[-1][0] < val:
            cnt += self.queue.pop()[1] + 1
        self.queue.append([val, cnt])

    def pop(self):
        if self.queue[0][1] > 0:
            self.queue[0][1] -= 1
            return
        return self.queue.popleft()[0]

    @property
    def max(self):
        return self.queue[0][0]


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        q = Monoqueue()
        n = len(nums)
        for i in range(k-1):
            q.push(nums[i])
            print q.queue

        res = []
        for i in range(k-1, n):
            q.push(nums[i])
            res.append(q.max)
            print q.queue
            q.pop()

        return res


```

### deque

```python
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        
        stack = deque()
        
        for i in range(k-1):
            num = nums[i]
            count = 1
            while stack and stack[-1][1] < num:
                cnt, _ = stack.pop()
                count += cnt
            stack.append([count, num])
        
        res = []
        for i in range(k-1, len(nums)):
            num = nums[i]
            count = 1
            while stack and stack[-1][1] < num:
                cnt, _ = stack.pop()
                count += cnt
            stack.append([count, num])
            
            res.append(stack[0][1])
            stack[0][0] -= 1
            if stack[0][0] == 0:
                stack.popleft()
        
        return res                
```


## refs

* [leetcode](https://leetcode.com/problems/sliding-window-maximum/discuss/65885/This-is-a-typical-monotonic-queue-problem)
* [article](https://medium.com/algorithms-and-leetcode/monotonic-queue-explained-with-leetcode-problems-7db7c530c1d6)

## schedule

* [x] 2019/10/22
* [x] 2019/10/23
* [x] 2019/12/21
* [x] 2020/01/07
* [ ] 2020/01/08
