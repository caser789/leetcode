---
tags: [2019/09/14, leetcode/884]
title: Uncommon Words from Two Sentences
created: '2019-09-07T08:24:21.824Z'
modified: '2019-09-11T14:18:40.951Z'
---

# Uncommon Words from Two Sentences

We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



### Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

### Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]


## Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.

## Solution

```python
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        kv = {}
        for w in A.split(' '):
            kv.setdefault(w, 0)
            kv[w] += 1
        for w in B.split(' '):
            kv.setdefault(w, 0)
            kv[w] += 1
        return [k for k, v in kv.items() if v == 1]
```

## schedule

* [x] 0 2019/09/10
* [x] 1 2019/09/11
* [ ] 1 2019/09/14
