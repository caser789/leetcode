---
tags: [2019/08/26, data structure/map, leetcode/1160, method/search/hash]
title: Find Words That Can Be Formed by Characters
created: '2019-08-26T14:12:51.022Z'
modified: '2019-08-26T14:19:37.148Z'
---

# Find Words That Can Be Formed by Characters

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

### Example 1:

```
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation:
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
```

### Example 2:

```
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation:
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
```

> 1 <= words.length <= 1000
> 1 <= words[i].length, chars.length <= 100
> All strings contain lowercase English letters only.


## Solution

```python
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        counter = {}
        for c in chars:
            counter.setdefault(c, 0)
            counter[c] += 1

        res = 0
        for word in words:
            res +=  self.is_good(word, dict(counter))
        return res

    def is_good(self, word, counter):
        n = 0
        for c in word:
            if c not in counter:
                return 0
            if counter[c] == 0:
                return 0
            counter[c] -= 1
            n += 1
        return n
```
