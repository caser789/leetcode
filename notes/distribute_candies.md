---
tags: [2019/11/02, leetcode/575]
title: Distribute Candies
created: '2019-09-07T08:25:29.027Z'
modified: '2019-10-19T13:19:07.884Z'
---

# Distribute Candies

Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.

### Example 1:

Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too.
The sister has three different kinds of candies.

### Example 2:

Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1].
The sister has two different kinds of candies, the brother has only one kind of candies.

## Note:

The length of the given array is in range [2, 10,000], and will be even.
The number in given array is in range [-100,000, 100,000].

## Solution

```python
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candies.sort()
        cnt = 1
        i = 1
        while i < len(candies) and cnt < len(candies)/2:
            if candies[i] > candies[i-1]:
                cnt += 1
            i += 1
        return cnt
```

## schedule

* [x] 0 2019/09/11
* [x] 1 2019/09/12
* [x] 1 2019/09/15
* [x] 1 2019/09/22
* [x] 1 2019/10/07
* [x] 1 2019/10/08
* [x] 1 2019/10/11
* [x] 1 2019/10/18
* [ ] 1 2019/11/02
