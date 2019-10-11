---
tags: [2019/10/13, leetcode/1189, method/index]
title: Maximum Number of Balloons
created: '2019-10-08T15:05:17.974Z'
modified: '2019-10-10T13:16:34.440Z'
---

# Maximum Number of Balloons

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 10^4
text consists of lower case English letters only.

## Solution

```python
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        lst = [0] * 26
        for c in text:
            i = ord(c) - ord('a')
            lst[i] += 1
        
        cnt = 0
        done = False
        while not done:
            
            for c in 'balloon':
                i = ord(c) - ord('a')
                if lst[i] == 0:
                    done = True
                    break
                lst[i] -= 1
            if not done:
                cnt += 1
        return cnt
        
```

## schedule

* [x] 1 2019/10/09
* [x] 1 2019/10/10
* [ ] 1 2019/10/13
