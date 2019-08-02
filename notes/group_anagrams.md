---
title: Group Anagrams
created: '2019-08-01T05:41:53.092Z'
modified: '2019-08-01T05:42:16.141Z'
---

# Group Anagrams

Given an array of strings, group anagrams together.

### Example:

```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

> All inputs will be in lowercase.
> The order of your output does not matter.


## Solution

```python
class Solution(object):
    def groupAnagrams(self, strs):
        """
        >>> Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        [['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']]
        """
        store = {}
        for s in strs:
            key = tuple(sorted(s))
            store.setdefault(key, [])
            store[key].append(s)
        return [v for k, v in store.items()]
```
