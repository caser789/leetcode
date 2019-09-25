---
tags: [2019/10/08, data structure/trie, leetcode/720]
title: Longest Word in Dictionary
created: '2019-09-07T08:44:41.517Z'
modified: '2019-09-23T05:20:27.781Z'
---

# Longest Word in Dictionary

Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.

### Example 1:
Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

### Example 2:
Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

## Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].


## Solution

```python
import collections

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True
        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i

        stack = trie.values()
        res = ''
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(res) or len(word) == len(res) and word < res:
                    res = word
                stack.extend([cur[letter] for letter in cur if letter != END])
        return res
```

## schedule

* [x] 0 2019/09/12
* [x] 1 2019/09/13
* [x] 1 2019/09/16
* [x] 1 2019/09/23
* [ ] 1 2019/10/08
