---
tags: [2019/10/16, leetcode/754]
title: Reach a Number
created: '2019-09-24T15:27:35.413Z'
modified: '2019-10-13T05:24:33.842Z'
---

# Reach a Number

You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
Note:
target will be a non-zero integer in the range [-10^9, 10^9].

## Solution

```python
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target < 0:
            target = -target
        
        i = 0
        while target > 0:
            i += 1
            target -= i
            
        return i if target % 2 == 0 else i + 1 + i%2
        
```

## schedule

* [x] 0 2019/10/11
* [x] 1 2019/10/12
* [x] 1 2019/10/13
* [ ] 1 2019/10/16
