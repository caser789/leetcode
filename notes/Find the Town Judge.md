---
tags: [2019/11/03, leetcode/997]
title: Find the Town Judge
created: '2019-10-08T14:56:44.746Z'
modified: '2019-10-27T04:48:26.360Z'
---

# Find the Town Judge

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
 

## Note:

1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N
Accepted

## Solution

```python
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if not trust:
            return 1
        truster = set()
        trustee = {}
        
        for x, y in trust:
            truster.add(x)
            trustee.setdefault(y, 0)
            trustee[y] += 1
        
        p = None
        for k, v in trustee.items():
            if v == N-1:
                if p is None:
                    p = k
                else:
                    return -1
        if p is None:
            return -1
        
        if p in truster:
            return -1
        return p
            
        
```

```python
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        counter = [0] * (N+1)
        for i, j in trust:
            counter[i] -= 1
            counter[j] += 1
        
        for i in range(1, N+1):
            if counter[i] == N-1:
                return i
        return -1
```

## schedule

* [x] 1 2019/10/09
* [x] 1 2019/10/10
* [x] 1 2019/10/13
* [x] 1 2019/10/20
* [x] 1 2019/10/24
* [x] 1 2019/10/27
* [ ] 1 2019/11/03
