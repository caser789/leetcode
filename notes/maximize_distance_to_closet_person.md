---
tags: [2019/08/30, leetcode/849, TODO]
title: Maximize Distance to Closest Person
created: '2019-08-30T14:35:12.089Z'
modified: '2019-08-30T14:43:33.225Z'
---

# Maximize Distance to Closest Person

In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to closest person.

### Example 1:

```
Input: [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
```

### Example 2:

```
Input: [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
```

> 1 <= seats.length <= 20000
> seats contains only 0s or 1s, at least one 0, and at least one 1.

## Solution

### 2 arrays

```python
class Solution(object):
    def maxDistToClosest(self, digits):
        """
        :type seats: List[int]
        :rtype: int
        """
        n = len(digits)
        left = [n] * n
        right = [n] * n

        for i in range(n):
            if digits[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i-1] + 1

        for i in range(n-1, -1, -1):
            if digits[i] == 1:
                right[i] = 0
            elif i < n - 1:
                right[i] = right[i+1] + 1

        return max(min(left[i], right[i]) for i, digit in enumerate(digits) if not digit)
```

### 2 pointers

```python
class Solution(object):
    def maxDistToClosest(self, digits):
        """
        :type seats: List[int]
        :rtype: int
        """
        people = (i for i, digit in enumerate(digits) if digit)
        prev, future = None, next(people)

        res = 0
        for i, digit in enumerate(digits):
            if digit == 1:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)

                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i

                res = max(res, min(left, right))
        return res
```

### groupby

```python
import itertools
class Solution(object):
    def maxDistToClosest(self, digits):
        """
        :type seats: List[int]
        :rtype: int
        """
        res = 0
        for seat, group in itertools.groupby(digits):
            if not seat:
                k = len(list(group))
                res = max(res, (k+1)/2)
        return max(res, digits.index(1), digits[::-1].index(1))

```
