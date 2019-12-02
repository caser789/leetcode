---
tags: [2019/11/04, leetcode/765, method/union find]
title: Couples Holding Hands
created: '2019-10-31T14:21:49.202Z'
modified: '2019-11-01T05:23:56.356Z'
---

# Couples Holding Hands

N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.
Note:

len(row) is even and in the range of [4, 60].
row is guaranteed to be a permutation of 0...len(row)-1.


## Solution

```python
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
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
    def __len__(self):
        return self.n

class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        n = len(row)
        m = n / 2
        uf = UF(m)
        for i in range(m):
            a = row[i*2]
            b = row[i*2+1]
            uf.union(a/2, b/2)
        
        return m - len(uf)
        
```

## schedule

* [x] 2019/10/31
* [x] 2019/11/01
* [ ] 2019/11/04
