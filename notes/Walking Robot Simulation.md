---
tags: [2019/11/03, leetcode/874]
title: Walking Robot Simulation
created: '2019-10-08T14:52:35.897Z'
modified: '2019-10-27T04:30:17.702Z'
---

# Walking Robot Simulation

A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles. 

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.

 

Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)
 

## Note:

0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
The answer is guaranteed to be less than 2 ^ 31.

## Solution

```python
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        s = set(map(tuple, obstacles))
        res = 0
        
        for cmd in commands:
            if cmd == -2:  # left
                di = (di-1) % 4
            elif cmd == -1:  # right
                di = (di + 1) % 4
            else:
                for k in range(cmd):
                    if (x+dx[di], y+dy[di]) not in s:
                        x += dx[di]
                        y += dy[di]
                        res = max(res, x*x+y*y)
        return res
                    
        
```

## schedule

* [x] 0 2019/10/12
* [x] 1 2019/10/13
* [x] 1 2019/10/16
* [x] 1 2019/10/23
* [x] 1 2019/10/24
* [x] 1 2019/10/27
* [ ] 1 2019/11/03
