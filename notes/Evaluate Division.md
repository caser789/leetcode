---
tags: [2020/01/02, leetcode/399, method/union find]
title: Evaluate Division
created: '2020-01-02T13:48:03.347Z'
modified: '2020-01-02T13:49:32.431Z'
---

# Evaluate Division

Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

## Solution

```python
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        i = 0
        c_to_i = {}
        for a, b in equations:
            for x in (a, b):
                if x not in c_to_i:
                    c_to_i[x] = i
                    i += 1
        uf = UF(i)

        for i, value in enumerate(values):
            a, b = equations[i]
            uf.union(c_to_i[a], c_to_i[b], value)

        res = []
        for a, b in queries:
            if a not in c_to_i or b not in c_to_i:
                res.append(-1.0)
            else:
                i = c_to_i[a]
                j = c_to_i[b]
                ii, x  = uf.find(i)
                jj, y  = uf.find(j)
                if ii != jj:
                    res.append(-1.0)
                else:
                    res.append(x / y)
        return res


class UF(object):
    def __init__(self, n):
        self.parents = range(n)
        self.weights = [1] * n

    def find(self, p):
        i = p
        w = 1
        while p != self.parents[p]:
            w *= self.weights[p] * self.weights[self.parents[p]]
            self.weights[p] *= self.weights[self.parents[p]]
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p, w

    def union(self, p, q, v):
        a, i = self.find(p)
        b, j = self.find(q)
        if a == b:
            return

        self.parents[a] = b
        self.weights[a] = v * j / i

    def weight(self, p):
        w = self.weights[p]
        while p != self.parents[p]:
            p = self.parents[p]
            w *= self.weights[p]
        w *= self.weights[p]
        return w
```

## schedule

* [x] 2020/01/02
* [ ] 2020/01/03

## refs

* [lc](https://leetcode.com/problems/evaluate-division/)
