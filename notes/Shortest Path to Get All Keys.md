---
tags: [2019/12/23, data structure/priority queue, leetcode/864]
title: Shortest Path to Get All Keys
created: '2019-12-17T14:24:31.074Z'
modified: '2019-12-22T03:28:45.678Z'
---

# Shortest Path to Get All Keys

We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@" is the starting point, ("a", "b", ...) are keys, and ("A", "B", ...) are locks.

We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.  We cannot walk outside the grid, or walk into a wall.  If we walk over a key, we pick it up.  We can't walk over a lock unless we have the corresponding key.

For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the first K letters of the English alphabet in the grid.  This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys.  If it's impossible, return -1.

 

### Example 1:

Input: ["@.a.#","###.#","b.A.B"]
Output: 8
Example 2:

Input: ["@..aA","..B#.","....b"]
Output: 6
 

### Note:

1 <= grid.length <= 30
1 <= grid[0].length <= 30
grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F'
The number of keys is in [1, 6].  Each key has a different letter and opens exactly one lock.

## Solution

```python
import collections


class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        key_cnt = 0
        moves = set()
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '@':
                    start_i = i
                    start_j = j
                elif grid[i][j] in 'abcdef':
                    key_cnt += 1
        
        deque = collections.deque()
        deque.append([start_i, start_j, 0, ".@abcdef", 0])
        
        while deque:
            i, j, steps, keys, collected_keys = deque.popleft()
            
            if grid[i][j] in "abcdef" and grid[i][j].upper() not in keys:
                keys += grid[i][j].upper()
                collected_keys += 1
            
            if collected_keys == key_cnt:
                return steps
            
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < n and 0 <= y < m and grid[x][y] in keys:
                    if (x, y, keys) not in moves:
                        moves.add((x, y, keys))
                        deque.append([x, y, steps+1, keys, collected_keys])
        return -1
```

## refs

* [lc](https://leetcode.com/problems/shortest-path-to-get-all-keys/)

## schedule

* [x] 2019/20/18
* [x] 2019/12/22
* [ ] 2019/12/23
