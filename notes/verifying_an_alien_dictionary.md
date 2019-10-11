---
tags: [2019/10/12, leetcode/953]
title: Verifying an Alien Dictionary
created: '2019-09-07T08:29:50.510Z'
modified: '2019-10-09T14:39:25.562Z'
---

# Verifying an Alien Dictionary

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.



### Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

### Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

### Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


## Note:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are english lowercase letters.

## Solution

```python
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_index = {c:i for i, c in enumerate(order)}

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            for k in range(min(len(word1), len(word2))):
                if word1[k] != word2[k]:
                    if order_index[word1[k]] > order_index[word2[k]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True
```

## schedule

* [x] 0 2019/09/11
* [x] 1 2019/09/12
* [x] 1 2019/09/13
* [x] 1 2019/09/16
* [x] 1 2019/09/23
* [x] 1 2019/10/08
* [x] 1 2019/10/09
* [ ] 1 2019/10/12
