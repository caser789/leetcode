---
tags: [2019/08/17, leetcode/338, method/dp]
title: Counting Bits
created: '2019-08-17T09:42:24.494Z'
modified: '2019-08-17T09:42:54.772Z'
---

# Counting Bits


Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

### Example 1:

```
Input: 2
Output: [0,1,1]
```

### Example 2:

```
Input: 5
Output: [0,1,1,2,1,2]
```

## Follow up:

* It is very easy to come up with a solution with run time O(n*sizeof(integer)).
* But can you do it in linear time O(n) /possibly in a single pass?
* Space complexity should be O(n).
* Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

## Solution

```python
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        if num == 1:
            return [0, 1]
        index = 2
        i = 0
        dp = [0] * (num+1)
        dp[1] = 1
        for j in range(2, num+1):
            if i == index:
                index *= 2
                i = 0
            dp[j] = dp[i] + 1
            i += 1
        return dp[num]
```
