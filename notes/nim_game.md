---
tags: [2019/10/20, leetcode/292]
title: Nim Game
created: '2019-09-22T11:12:48.088Z'
modified: '2019-10-07T05:00:26.806Z'
---

# Nim Game

You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

Example:

Input: 4
Output: false 
Explanation: If there are 4 stones in the heap, then you will never win the game;
             No matter 1, 2, or 3 stones you remove, the last stone will always be 
             removed by your friend.

## Solution

```python
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0
```

## schedule

* [x] 0 2019/09/24
* [x] 1 2019/09/25
* [x] 1 2019/09/28
* [x] 1 2019/10/05
* [ ] 1 2019/10/20
