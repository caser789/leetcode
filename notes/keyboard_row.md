---
tags: [2019/10/06, leetcode/500]
title: Keyboard Row
created: '2019-09-07T08:20:26.735Z'
modified: '2019-09-22T09:48:51.009Z'
---

# Keyboard Row

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


![pic](https://assets.leetcode.com/uploads/2018/10/12/keyboard.png)



### Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]


## Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

## Solution

```python
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        kv = {
            1: 'qwertyuiop',
            2: 'asdfghjkl',
            3: 'zxcvbnm',
        }

        store = {}
        for k, v in kv.items():
            for c in v:
                store[c] = k
                store[c.upper()] = k

        def same_row(word):
            r = store[word[0]]
            for c in word[1:]:
                if store[c] != r:
                    return False
            return True

        return [w for w in words if same_row(w)]
```

## schedule

* [x] 0 2019/09/10
* [x] 1 2019/09/11
* [x] 1 2019/09/14
* [x] 1 2019/09/21
* [ ] 1 2019/10/06
