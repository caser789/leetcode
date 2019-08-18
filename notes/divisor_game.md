---
tags: [2019/08/18, leetcode/1025, method/math]
title: Divisor Game
created: '2019-08-18T10:03:49.947Z'
modified: '2019-08-18T10:05:07.514Z'
---

# Divisor Game

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.

### Example 1:

```
Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
```

### Example 2:

```
Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
```

## Prerequiste

3 "definites" you need to know

* Anyone who gets 1 definitely loses since not exist a x in range of (0, 1)
* Anyone who gets 2 definitely wins since he always/or only can make 2 become 1. Because x can only be 1, 2 % 1 == 0 and 2 - 1 = 1
* For any N >= 2, N will definitely be reduced to 2

  Just illustrate some N below. Based on the "chain", you can see, no matter what N starts, all leads to 2 in the end:

  //  2 -> 1
      3 -> 2
  //  4 -> 2, 3
      5 -> 4
  //  6 -> 3, 4, 5
  	  7 -> 6
  //  8 -> 4, 6, 7
      9 -> 6, 8
  //  10 -> 5, 8, 9
      11 -> 10
  //  12 -> 8, 9, 10, 11
  	  13 -> 12
  //  14 -> 7, 12, 13
  	  15 -> 10, 12
  //  16 -> 8, 12, 14
  	  17 -> 16
  //  18 -> 9, 12, 15, 16
  	  19 -> 18
  //  20 -> 10, 15, 16, 18
  ...

## Strategy

```
So Alice and Bob both say: Give me 2! They fight for 2 and it becomes the point of their "life". But how can they gurantee that they can get 2?

However after study, they find out:

For odd N, no matter what x is, x must be odd, then N - x must be even, i.e. odd =< even
For even N, we can always choose x as 1, then N - x = N - 1 must be odd, even => odd

They get the conclusion:

The one who gets even number `N` has the choice to get all the even numbers including 2(since 2 is even), so here comes win.
So if N is even initially,
1. What is Alice's optimal strategy?
Choose x = 1, N = N - 1, send the odd back to Bob
2. What is Bob's optimal strategy?
Choose x as large as possible to make N reduce as fast as possible such that the pain can end as early as possible, since nothing will change the fact that he will lose. Just don't suffer.


From above, we know that if Alice meets even N, she will win. So we just need to check if N is divisble by 2.
```


> 1 <= N <= 1000

```
class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return N % 2 == 0
```
