---
tags: [2019/11/02, leetcode/1202, method/union find]
title: Smallest String With Swaps
created: '2019-10-29T00:57:10.418Z'
modified: '2019-10-30T05:01:28.912Z'
---

# Smallest String With Swaps

You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

 

Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"
Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"
 

Constraints:

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.

## Solution

```python
import heapq
from collections import defaultdict


class UF(object):

    def __init__(self, n):
        self.n = n
        self.parents = range(n)

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        self.parents[root_q] = root_p
        self.n -= 1

    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p


class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        n = len(s)
        uf = UF(n)
        for i, j in pairs:
            uf.union(i, j)

        kv = defaultdict(list)
        for i, c in enumerate(s):
            root = uf.find(i)
            heapq.heappush(kv[root], c)

        res = []
        for i in range(n):
            root = uf.find(i)
            c = heapq.heappop(kv[root])
            res.append(c)
        return ''.join(res)

        
```

## schedule

* [x] 2019/10/29
* [x] 2019/10/30
* [ ] 2019/11/02
