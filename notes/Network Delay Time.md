---
tags: [2019/12/14, data structure/graph, data structure/priority queue, leetcode/743, method/djikstra]
title: Network Delay Time
created: '2019-12-14T10:58:49.817Z'
modified: '2019-12-14T14:38:57.664Z'
---

# Network Delay Time

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

 

Example 1:

![pic](https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png)

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
 

Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.

## Solution

### heapq

```python
import heapq


class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        node_to_neis = {}
        for u, v, w in times:
            node_to_neis.setdefault(u, [])
            node_to_neis[u].append((v, w))

        seen = {}
        pq = [(0, K)]
        while pq:
            time, node = heapq.heappop(pq)
            if node in seen: continue
            seen[node] = time
            if node not in node_to_neis: continue
            for nei, t in node_to_neis[node]:
                heapq.heappush(pq, (time+t, nei))

        return max(seen.values()) if len(seen) == N else -1


```

## refs

* [solution](https://leetcode.com/problems/network-delay-time/discuss/187713/Python-concise-queue-and-heap-solutions)
* [lc](https://leetcode.com/problems/network-delay-time/)
