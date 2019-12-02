---
tags: [2019/11/19, leetcode/942]
title: DI String Match
created: '2019-09-22T11:04:37.555Z'
modified: '2019-10-19T13:25:19.447Z'
---

# DI String Match

Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]


### Example 1:

Input: "IDID"
Output: [0,4,1,3,2]

### Example 2:

Input: "III"
Output: [0,1,2,3]

### Example 3:

Input: "DDI"
Output: [3,2,0,1]


## Note:

1 <= S.length <= 10000
S only contains characters "I" or "D".

## Solution

```python
class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lo = 0
        hi = len(S)
        res = []
        for c in S:
            if c == 'I':
                res.append(lo)
                lo += 1
            else:
                res.append(hi)
                hi -= 1
        res.append(lo)
        return res
```

## schedule

* [x] 0 2019/09/23
* [x] 1 2019/09/24
* [x] 1 2019/09/27
* [x] 1 2019/10/04
* [x] 1 2019/10/19
* [ ] 1 2019/11/19
