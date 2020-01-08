---
tags: [2020/01/06, leetcode/952, method/union find]
title: Largest Component Size by Common Factor
created: '2020-01-05T05:09:21.839Z'
modified: '2020-01-05T05:10:55.410Z'
---

# Largest Component Size by Common Factor

Given a non-empty array of unique positive integers A, consider the following graph:

There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

 

Example 1:

![pic](https://assets.leetcode.com/uploads/2018/12/01/ex1.png)

Input: [4,6,15,35]
Output: 4

Example 2:

![pic](https://assets.leetcode.com/uploads/2018/12/01/ex2.png)

Input: [20,50,9,63]
Output: 2

Example 3:

![pic](https://assets.leetcode.com/uploads/2018/12/01/ex3.png)

Input: [2,3,6,7,4,12,21,39]
Output: 8

Note:

1 <= A.length <= 20000
1 <= A[i] <= 100000

## Solution

```python
class Solution(object):
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        uf = UF(n)

        factor_to_index = {}
        for i in range(n):
            a = A[i]
            j = 2
            while j*j <= a:
                if a % j == 0:
                    if j not in factor_to_index:
                        factor_to_index[j] = i
                    else:
                        uf.union(i, factor_to_index[j])

                    if a / j not in factor_to_index:
                        factor_to_index[a/j] = i
                    else:
                        uf.union(i, factor_to_index[a/j])
                j += 1

            if a not in factor_to_index:
                factor_to_index[a] = i
            else:
                uf.union(i, factor_to_index[a])
        return uf.max


class UF(object):
    def __init__(self, n):
        self.n = n
        self.parents = range(n)
        self.ranks = [0] * n
        self.sizes = [1] * n
        self.max = 1

    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p

    def union(self, p, q):
        u = self.find(p)
        v = self.find(q)
        if u == v:
            return

        if self.ranks[u] < self.ranks[v]:
            self.parents[u] = v
            self.sizes[v] += self.sizes[u]
            self.max = max(self.max, self.sizes[v])
        elif self.ranks[v] < self.ranks[u]:
            self.parents[v] = u
            self.sizes[u] += self.sizes[v]
            self.max = max(self.max, self.sizes[u])
        else:
            self.parents[u] = v
            self.ranks[v] += 1
            self.sizes[v] += self.sizes[u]
            self.max = max(self.max, self.sizes[v])

        self.n -= 1

```

## schedule

* [x] 2020/01/05
* [ ] 2020/01/06

## refs

* [lc](https://leetcode.com/problems/largest-component-size-by-common-factor/)
