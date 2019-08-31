---
tags: [2019/09/02, leetcode/520, TODO]
title: Detect Capital
created: '2019-08-31T09:06:38.843Z'
modified: '2019-08-31T09:06:49.908Z'
---

# Detect Capital

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

* All letters in this word are capitals, like "USA".
* All letters in this word are not capitals, like "leetcode".
* Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.


### Example 1:

Input: "USA"
Output: True


### Example 2:

Input: "FlaG"
Output: False


## Note:

* The input will be a non-empty word consisting of uppercase and lowercase latin letters.


## Solution

```python
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

```
