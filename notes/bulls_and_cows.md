---
tags: [2019/11/09, leetcode/299, method/index]
title: Bulls and Cows
created: '2019-09-07T08:55:35.163Z'
modified: '2019-10-08T14:38:21.634Z'
---

# Bulls and Cows

You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows.

Please note that both secret number and friend's guess may contain duplicate digits.

### Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

### Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.

## Note:
You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.


## Solution

```python
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        count = [0] * 10
        for digit in secret:
            i = ord(digit) - ord('0')
            count[i] += 1
        bull = 0
        cow = 0
        for a, b in zip(secret, guess):
            if a == b:
                bull += 1
                i = ord(a) - ord('0')
                count[i] -= 1

        for i in range(len(guess)):
            if secret[i] == guess[i]:
                continue
            digit = guess[i]
            j = ord(digit) - ord('0')
            if count[j] == 0:
                continue
            cow += 1
            count[j] -= 1

        return '{}A{}B'.format(bull, cow)
```

## schedule

* [x] 0 2019/09/13
* [x] 1 2019/09/14
* [x] 1 2019/09/17
* [x] 1 2019/09/24
* [x] 1 2019/10/09
* [ ] 1 2019/11/09
