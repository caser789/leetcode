---
tags: [2019/11/11, leetcode/914]
title: X of a Kind in a Deck of Cards
created: '2019-10-08T14:55:21.976Z'
modified: '2019-10-27T04:26:27.357Z'
---

# X of a Kind in a Deck of Cards

In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
 

Example 1:

Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
Example 2:

Input: [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
Example 3:

Input: [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: [1,1]
Output: true
Explanation: Possible partition [1,1]
Example 5:

Input: [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]

## Note:

1 <= deck.length <= 10000
0 <= deck[i] < 10000
 

## Solution

```python
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        counter = {}
        for num in deck:
            counter.setdefault(num, 0)
            counter[num] += 1
        
        n = len(deck)
        for i in range(2, n+1):
            if n % i == 0:
                if all(v % i == 0 for v in counter.values()):
                    return True
        return False
        
```

## schedule

* [x] 0 2019/10/12
* [x] 1 2019/10/13
* [x] 1 2019/10/16
* [x] 1 2019/10/17
* [x] 1 2019/10/20
* [x] 1 2019/10/27
* [ ] 1 2019/11/11
