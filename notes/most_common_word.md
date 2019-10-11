---
tags: [2019/10/31, leetcode/819]
title: Most Common Word
created: '2019-08-31T09:18:03.909Z'
modified: '2019-10-02T05:30:34.708Z'
---

# Most Common Word

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

### Example:

Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"

Explanation:

"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.

Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.


## Note:

* 1 <= paragraph.length <= 1000.
* 0 <= banned.length <= 100.
* 1 <= banned[i].length <= 10.
* The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
* paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
* There are no hyphens or hyphenated words.
* Words only consist of letters, never apostrophes or other punctuation symbols.

## Solution

```python
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        
        chars = set('!?\',;.')
        
        max_cnt = 0
        word_to_cnt = {}
        
        res = []
        for c in paragraph:
            if c in set({' ', '.', ','}):
                w = ''.join(res)
                if w in banned:
                    res = []
                    continue
                if not w:
                    res = []
                    continue
                word_to_cnt.setdefault(w, 0)
                word_to_cnt[w] += 1
                max_cnt = max(max_cnt, word_to_cnt[w])
                
                res = []
            elif c in chars:
                continue
            else:
                res.append(c.lower())
        
        w = ''.join(res)
        if w not in banned and w:
            word_to_cnt.setdefault(w, 0)
            word_to_cnt[w] += 1
            max_cnt = max(max_cnt, word_to_cnt[w])
        
        for k, v in word_to_cnt.items():
            if v == max_cnt:
                return k
                
```

## schedule

* [x] 0 2019/09/04
* [x] 1 2019/09/05
* [x] 1 2019/09/08
* [x] 1 2019/09/15
* [x] 1 2019/09/30
* [ ] 1 2019/10/31
