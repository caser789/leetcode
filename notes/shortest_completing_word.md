---
tags: [2019/10/08, leetcode/748]
title: Shortest Completing Word
created: '2019-09-07T08:32:39.530Z'
modified: '2019-09-23T14:27:42.330Z'
---

# Shortest Completing Word

Find the minimum length word from a given dictionary words, which has all the letters from the string licensePlate. Such a word is said to complete the given string licensePlate

Here, for letters we ignore case. For example, "P" on the licensePlate still matches "p" on the word.

It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in the array.

The license plate might have the same letter occurring multiple times. For example, given a licensePlate of "PP", the word "pair" does not complete the licensePlate, but the word "supper" does.

### Example 1:
Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
Output: "steps"
Explanation: The smallest length word that contains the letters "S", "P", "S", and "T".
Note that the answer is not "step", because the letter "s" must occur in the word twice.
Also note that we ignored case for the purposes of comparing whether a letter exists in the word.

### Example 2:
Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
Output: "pest"
Explanation: There are 3 smallest length words that contains the letters "s".
We return the one that occurred first.

## Note:
licensePlate will be a string with length in range [1, 7].
licensePlate will contain digits, spaces, or letters (uppercase or lowercase).
words will have a length in the range [10, 1000].
Every words[i] will consist of lowercase letters, and have length in range [1, 15].

## Solution

```python
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        def match(word, indexes):
            lst = [0] * 26
            for c in word:
                if not c.isalpha():
                    continue
                i = ord(c.lower()) - ord('a')
                lst[i] += 1
            for i in range(26):
                if indexes[i] < lst[i]:
                    return False
            return True


        indexes = [0] * 26
        for c in licensePlate:
            if not c.isalpha():
                continue
            i = ord(c.lower()) - ord('a')
            indexes[i] += 1
        min_length = 999999999
        result = None
        for word in words:
            n = len(word)
            if match(word, indexes) and n < min_length:
                min_length = n
                result = word
```

## schedule

* [x] 0 2019/09/11
* [x] 1 2019/09/12
* [x] 1 2019/09/13
* [x] 1 2019/09/16
* [x] 1 2019/09/23
* [ ] 1 2019/10/08
