---
tags: [2019/09/01, leetcode/893, method/index]
title: Groups of Special-Equivalent Strings
created: '2019-08-31T08:48:31.799Z'
modified: '2019-09-01T04:25:50.318Z'
---

# Groups of Special-Equivalent Strings

You are given an array A of strings.

Two strings S and T are special-equivalent if after any number of moves, S == T.

A move consists of choosing two indices i and j with i % 2 == j % 2, and swapping S[i] with S[j].

Now, a group of special-equivalent strings from A is a non-empty subset S of A such that any string not in S is not special-equivalent with any string in S.

Return the number of groups of special-equivalent strings from A.

### Example 1:

Input: ["a","b","c","a","c","c"]
Output: 3
Explanation: 3 groups ["a","a"], ["b"], ["c","c","c"]

### Example 2:

Input: ["aa","bb","ab","ba"]
Output: 4
Explanation: 4 groups ["aa"], ["bb"], ["ab"], ["ba"]

### Example 3:

Input: ["abc","acb","bac","bca","cab","cba"]
Output: 3
Explanation: 3 groups ["abc","cba"], ["acb","bca"], ["bac","cab"]

### Example 4:

Input: ["abcd","cdab","adcb","cbad"]
Output: 1
Explanation: 1 group ["abcd","cdab","adcb","cbad"]


> 1 <= A.length <= 1000
> 1 <= A[i].length <= 20
> All A[i] have the same length.
> All A[i] consist of only lowercase letters.

## Solution

### intuitive

```python
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        s = {}
        for word in A:
            k = self.get_key(word)
            s.setdefault(k, [])
            s[k].append(word)
        return len(s)

    def get_key(self, word):
        lst1 = list(word[::2])
        lst2 = list(word[1::2])
        lst1.sort()
        lst2.sort()
        return tuple(lst1), tuple(lst2)
```

### better

```python
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        s = set()
        for word in A:
            s.add(self.get_key(word))
        return len(s)

    def get_key(self, word):
        res = [0] * 52
        for i, c in enumerate(word):
            index = ord(c) - ord('a') + 26 * (i%2)
            res[index] += 1
        return tuple(res)
```
