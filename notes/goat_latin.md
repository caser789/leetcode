---
tags: [2019/09/27, leetcode/824]
title: Goat Latin
created: '2019-08-31T08:50:50.639Z'
modified: '2019-09-12T11:40:40.271Z'
---

# Goat Latin

A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.

If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".

Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin.


### Example 1:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

### Example 2:

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"


## Notes:

* S contains only uppercase, lowercase and spaces. Exactly one space between each word.
* 1 <= S.length <= 150.

## Solution

### intuitive

```python
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split(' ')
        res = []
        vowels = {'a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U'}
        for i, word in enumerate(words):
            tmp = []
            if word[0] in vowels:
                tmp.append(word)
                tmp.append('ma')
            else:
                tmp.append(word[1:])
                tmp.append(word[0])
                tmp.append('ma')
            for _ in range(i+1):
                tmp.append('a')
            res.append(''.join(tmp))
        return ' '.join(res)
```

### better

```python
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split(' ')
        vowels = set({'a', 'o', 'i', 'e', 'u', 'A', 'O', 'I', 'E', 'U'})
        res = []
        for i, word in enumerate(words):
            w = []
            if word[0] in vowels:
                w.append(word)
            else:
                w.append(word[1:])
                w.append(word[0])
            w.append('ma')
            for _ in range(i+1):
                w.append('a')
            res.append(''.join(w))
        return ' '.join(res)
```

## schedule

* [x] 0 2019/09/01
* [x] 1 2019/09/02
* [x] 3 2019/09/05
* [x] 3 2019/09/12
* [ ] 3 2019/09/27

