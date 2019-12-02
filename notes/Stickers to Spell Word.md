---
tags: [2019/11/25, application/split-array, leetcode/691, method/backtrack]
title: Stickers to Spell Word
created: '2019-11-25T11:49:42.210Z'
modified: '2019-11-25T11:51:09.958Z'
---

# Stickers to Spell Word

We are given N different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given target string by cutting individual letters from your collection of stickers and rearranging them.

You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

What is the minimum number of stickers that you need to spell out the target? If the task is impossible, return -1.

Example 1:

Input:

["with", "example", "science"], "thehat"
Output:

3
Explanation:

We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
Example 2:

Input:

["notice", "possible"], "basicbasic"
Output:

-1
Explanation:

We can't form the target "basicbasic" from cutting letters from the given stickers.
Note:

stickers has length in the range [1, 50].
stickers consists of lowercase English words (without apostrophes).
target has length in the range [1, 15], and consists of lowercase English letters.
In all test cases, all words were chosen randomly from the 1000 most common US English words, and the target was chosen as a concatenation of two random words.
The time limit may be more challenging than usual. It is expected that a 50 sticker test case can be solved within 35ms on average.


## Solution

```python
class Solution(object):
    def minStickers(self, stickers, target):
        m = len(stickers)

        mp = [[0]*26 for y in range(m)]
        for i in range(m):
            for c in stickers[i]:
                mp[i][ord(c)-ord('a')] += 1

        dp = {}
        dp[""] = 0

        def helper(target):
            if target in dp:
                return dp[target]

            tar = [0] * 26
            for c in target:
                tar[ord(c)-ord('a')] += 1

            ans = float('inf')
            for i in xrange(m):
                if mp[i][ord(target[0])-ord('a')] == 0:
                    continue

                s = ''
                for j in range(26):
                    if tar[j] > mp[i][j]:
                        s += chr(ord('a')+j)*(tar[j] - mp[i][j])

                tmp = helper(s)
                if (tmp != -1):
                    ans = min(ans, 1+tmp)

            dp[target] = -1 if ans == float('inf') else ans
            return dp[target]

        return helper(target)

```

## refs

* [lc](https://leetcode.com/problems/stickers-to-spell-word/)


## schedule

* [ ] 2019/11/25
* [ ] 2019/11/26
