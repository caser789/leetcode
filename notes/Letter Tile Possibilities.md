---
tags: [2019/11/15, application/combination, leetcode/1079, method/backtrack]
title: Letter Tile Possibilities
created: '2019-11-15T04:40:47.677Z'
modified: '2019-11-25T08:55:37.706Z'
---

# Letter Tile Possibilities

You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.

 

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: "AAABBC"
Output: 188
 

Note:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.


## Solution

```
class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        res = set()
        n = len(tiles)

        def collect(seen, tmp):
            for i in range(n):
                if i in seen:
                    continue
                tmp.append(tiles[i])
                res.add(''.join(tmp))
                seen.add(i)

                collect(seen, tmp)

                tmp.pop()
                seen.remove(i)

        seen = set()
        tmp = []
        collect(seen, tmp)
        return len(res)


```

### better backtrack

```python
class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        tiles = list(tiles)
        tiles.sort()
        n = len(tiles)

        seen = [False] * n
        self.count = 0
        
        def search():
            self.count += 1
            
            for i in range(n):
                if seen[i]: continue
                if i > 0 and tiles[i] == tiles[i-1] and not seen[i-1] : continue
                seen[i] = True
                
                search()
                
                seen[i] = False
            
        search()
        return self.count - 1
        
```

## refs

* [lc](https://leetcode.com/problems/letter-tile-possibilities/)
