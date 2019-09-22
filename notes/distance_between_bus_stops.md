---
tags: [2019/09/24]
title: Distance Between Bus Stops
created: '2019-09-22T11:16:09.014Z'
modified: '2019-09-22T11:17:03.675Z'
---

# Distance Between Bus Stops

A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given start and destination stops.

 

Example 1:

![pic](https://assets.leetcode.com/uploads/2019/09/03/untitled-diagram-1.jpg)

Input: distance = [1,2,3,4], start = 0, destination = 1
Output: 1
Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.
 

Example 2:

![pic](https://assets.leetcode.com/uploads/2019/09/03/untitled-diagram-1-1.jpg)

Input: distance = [1,2,3,4], start = 0, destination = 2
Output: 3
Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.
 

Example 3:

![pic](https://assets.leetcode.com/uploads/2019/09/03/untitled-diagram-1-2.jpg)

Input: distance = [1,2,3,4], start = 0, destination = 3
Output: 4
Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.
 

Constraints:

1 <= n <= 10^4
distance.length == n
0 <= start, destination < n
0 <= distance[i] <= 10^4

## Solution

```
class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
```
