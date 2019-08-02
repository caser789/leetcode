---
tags: [hash]
title: Jewels and Stones
created: '2019-08-01T05:45:12.027Z'
modified: '2019-08-02T05:34:49.454Z'
---

# Jewels and Stones

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

### Example 1:

```
Input: J = "aA", S = "aAAbbbb"
Output: 3
```

### Example 2:

```
Input: J = "z", S = "ZZ"
Output: 0
```

> S and J will consist of letters and have length at most 50.
> The characters in J are distinct.


## Solution

```python
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        >>> J = "aA"
        >>> S = "aAAbbbb"
        >>> Solution().numJewelsInStones(J, S)
        3
        >>> J = "z"
        >>> S = "ZZ"
        >>> Solution().numJewelsInStones(J, S)
        0
        """
        s = set(J)
        cnt = 0
        for c in S:
            if c in s:
                cnt += 1
        return cnt
```
