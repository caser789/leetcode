---
tags: [2020/01/03, data structure/graph, data structure/tree, leetcode/684, method/traversal/dfs, method/union find]
title: Redundant Connection
created: '2019-08-11T05:25:05.084Z'
modified: '2020-01-02T14:09:14.550Z'
---

# Redundant Connection


In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

### Example 1:

```
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
```

### Example 2:

```
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
```

> The size of the input 2D-array will be between 3 and 1000.
> Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

## Solution

```python
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        last = None
        n = len(edges)
        uf = UF(n+1)
        for i, j in edges:
            if uf.is_connected(i, j):
                last = [i, j]
            else:
                uf.union(i, j)
        return last


class UF(object):

    def __init__(self, n):
        self.parents = range(n)
        self.n = n
        self.size = [0] * n

    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p

    def union(self, p, q):
        p_parent = self.find(p)
        q_parent = self.find(q)
        if p_parent == q_parent: return

        if self.size[p_parent] < self.size[q_parent]:
            self.parents[p_parent] = q_parent
        elif self.size[q_parent] < self.size[p_parent]:
            self.parents[q_parent] = p_parent
        else:
            self.parents[q_parent] = p_parent
            self.size[p_parent] += 1
        self.n -= 1

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
```

### dfs

```
import collections

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)
        
        def dfs(source, target):
            if source in seen: return
            
            seen.add(source)
            if source == target: return True
            return any(dfs(nei, target) for nei in graph[source])
        
        for u, v in edges:
            seen = set()
            
            if u in graph and v in graph and dfs(u, v):
                return u, v
            
            graph[u].add(v)
            graph[v].add(u)
```

## refs

* [lc](https://leetcode.com/problems/redundant-connection/)

## schedule

* [x] 2020/01/02
* [ ] 2020/01/03
