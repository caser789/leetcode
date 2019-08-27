---
tags: [2019/08/27, leetcode/1170]
title: Compare Strings by Frequency of the Smallest Character
created: '2019-08-27T15:37:58.107Z'
modified: '2019-08-27T15:38:18.747Z'
---

# Compare Strings by Frequency of the Smallest Character

Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

### Example 1:

```
Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
```

### Example 2:

```
Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").
```

> 1 <= queries.length <= 2000
> 1 <= words.length <= 2000
> 1 <= queries[i].length, words[i].length <= 10
> queries[i][j], words[i][j] are English lowercase letters.

## Solution

### intuition

```python
class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        _words = [self.count(word) for word in words]
        _queries = [self.count(q) for q in queries]
        res = []
        for q in _queries:
            cnt = 0
            for w in _words:
                if w > q:
                    cnt += 1
            res.append(cnt)
        return res


    def count(self, word):
        lst = [0] * 26
        for c in word:
            i = ord(c) - ord('a')
            lst[i] += 1
        for i in lst:
            if i:
                return i
```
