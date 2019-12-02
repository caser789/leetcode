---
tags: [2019/11/03, bit, leetcode/342]
title: Power of Four
created: '2019-09-24T15:03:57.103Z'
modified: '2019-10-27T04:40:46.088Z'
---

# Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?

## Solution

```python
class Solution(object):
    def __init__(self):
        mask = 0
        for i in range(0, 32, 2):
            mask |= (1 << i)
        self.mask = mask
        
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0: return False
        if num & (num-1): return False
        
        return num & self.mask == num 
        
```


## schedule

* [x] 0 2019/09/27
* [x] 1 2019/09/28
* [x] 1 2019/10/01
* [x] 1 2019/10/08
* [x] 1 2019/10/23
* [x] 1 2019/10/24
* [x] 1 2019/10/27
* [ ] 1 2019/11/03
