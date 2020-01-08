---
tags: [2020/01/03, leetcode/685, method/union find]
title: Redundant Connection II
created: '2020-01-02T14:37:34.648Z'
modified: '2020-01-02T14:38:43.869Z'
---

# Redundant Connection II

In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3
Example 2:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.


## Solution

```python
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = {}
        x = y = None
        
        for u, v in edges:
            if v in parent:
                x = [parent[v], v]
                y = [u, v]
                break
            parent[v] = u
            
        n = len(edges)
        uf = UF(n+1)
        
        for u, v in edges:
            if y is not None and u == y[0] and v == y[1]: continue
            if not uf.union(u, v):
                if x is None: return [u, v]
                return x
        return y
        
        
class UF(object):
    def __init__(self, n):
        self.n = n
        self.parents = range(n)
        self.ranks = [0] * n
    
    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p
    
    def union(self, p, q):
        u = self.find(p)
        v = self.find(q)
        if u == v:
            return False
        
        if self.ranks[u] < self.ranks[v]:
            self.parents[u] = v
        elif self.ranks[u] > self.ranks[v]:
            self.parents[v] = u
        else:
            self.parents[u] = v
            self.ranks[v] += 1
        self.n -= 1
        return True
```

## schedule

* [x] 2020/01/02
* [ ] 2020/01/03

## refs

* [lc](https://leetcode.com/problems/redundant-connection-ii/)
