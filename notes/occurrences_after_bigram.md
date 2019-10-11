---
tags: [2019/11/05, leetcode/1078, method/pointer]
title: Occurrences After Bigram
created: '2019-09-07T08:17:33.353Z'
modified: '2019-10-07T05:08:12.553Z'
---

# Occurrences After Bigram

Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.



### Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]

### Example 2:

Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]


## Note:

1 <= text.length <= 1000
text consists of space separated words, where each word consists of lowercase English letters.
1 <= first.length, second.length <= 10
first and second consist of lowercase English letters.


## Solution

```python
class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        words = text.split(' ')
        if len(words) < 3:
            return []

        a = words[0]
        b = words[1]
        res = []
        for i in range(2, len(words)):
            if a == first and b == second:
                res.append(words[i])

            a, b = b, words[i]

        return res
```

## schedule

* [x] 0 2019/09/09
* [x] 1 2019/09/10
* [x] 1 2019/09/13
* [x] 1 2019/09/20
* [x] 1 2019/10/05
* [ ] 1 2019/11/05
