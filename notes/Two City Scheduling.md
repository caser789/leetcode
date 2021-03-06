---
tags: [2019/11/07, leetcode/1029]
title: Two City Scheduling
created: '2019-10-08T14:59:25.210Z'
modified: '2019-10-23T11:16:49.751Z'
---

# Two City Scheduling

There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

## Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000
Accepted


## Solution

```python
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs)
        res = 0
        for i in range(n/2):
            res += costs[i][0]
            res += costs[i+n/2][1]
        return res
        
```


## schedule

* [x] 0 2019/10/12
* [x] 1 2019/10/13
* [x] 1 2019/10/16
* [x] 1 2019/10/23
* [ ] 1 2019/11/07
