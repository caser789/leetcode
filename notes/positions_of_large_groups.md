---
tags: [2019/08/28, application/array/status, leetcode/830, method/2 pointers]
title: Positions of Large Groups
created: '2019-08-28T15:39:08.334Z'
modified: '2019-08-28T15:53:18.747Z'
---

# Positions of Large Groups

In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.


### Example 1:

```
Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
```

### Example 2:

```
Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.
```

### Example 3:

```
Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
```

> 1 <= S.length <= 1000


## Solution

```python
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        prev = None
        start = 0
        end = 0
        cnt = 0
        max_cnt = 0
        res = []
        for i, c in enumerate(S):
            if c == prev:
                cnt += 1
                end = i
            else:
                if cnt >= 3:
                    res.append([start, end])
                start = i
                end = i
                prev = c
                cnt = 1
        if cnt >= 3:
            res.append([start, end])
        return res
```
