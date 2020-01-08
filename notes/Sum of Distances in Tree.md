---
favorited: true
tags: [2019/11/30, data structure/graph, leetcode/834, method/traversal/dfs/parent, TODO]
title: Sum of Distances in Tree
created: '2019-11-30T04:36:26.878Z'
modified: '2019-12-03T01:32:27.016Z'
---

# Sum of Distances in Tree

An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.

The ith edge connects nodes edges[i][0] and edges[i][1] together.

Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.

Example 1:

Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: 
Here is a diagram of the given tree:
  0
 / \
1   2
   /|\
  3 4 5
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.
Note: 1 <= N <= 10000

## Solution

```python
import collections


class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)        
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        count = [1] * N
        res = [0] * N
        
        def dfs(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    res[node] += res[child] + count[child]
        
        def dfs2(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    res[child] = res[node] - count[child] + N - count[child]
                    dfs2(child, node)

        dfs()
        dfs2()
        return res
```

## refs

* [lc](https://leetcode.com/problems/sum-of-distances-in-tree/)
* [solution](https://leetcode.com/problems/sum-of-distances-in-tree/solution/)
