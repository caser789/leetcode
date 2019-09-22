---
tags: [2019/09/14, leetcode/705]
title: Design HashSet
created: '2019-09-07T08:31:31.486Z'
modified: '2019-09-12T14:05:38.998Z'
---

# Design HashSet

Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet.
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

### Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);
hashSet.add(2);
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);
hashSet.contains(2);    // returns true
hashSet.remove(2);
hashSet.contains(2);    // returns false (already removed)

## Note:

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.


## Solution


```
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 8
        self.size = 0
        self.s = [None]*8
        self.lf = float(2)/3

    def myhash(self, key): # can be modified to hash other hashable objects like built in python hash function
        return key%self.capacity


    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if float(self.size)/self.capacity >= self.lf:
            self.capacity <<= 1
            ns = [None]*self.capacity
            for i in range(self.capacity >> 1):
                if self.s[i] and self.s[i] != "==TOMBSTONE==":
                    n = self.myhash(self.s[i])
                    while ns[n] is not None:
                        n = (5*n+1)%self.capacity
                    ns[n] = self.s[i]
            self.s = ns
        h = self.myhash(key)
        while self.s[h] is not None:
            if self.s[h] == key:
                return
            h = (5*h + 1) % self.capacity
            if self.s[h] == "==TOMBSTONE==":
                break
        self.s[h] = key
        self.size += 1



    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        h = self.myhash(key)
        while self.s[h]:
            if self.s[h] == key:
                self.s[h] = "==TOMBSTONE=="
                self.size -= 1
                return
            h = (5*h+1)%self.capacity


    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        h = self.myhash(key)
        while self.s[h] is not None:
            if self.s[h] == key:
                return True
            h = (5*h + 1)%self.capacity
        return False
```


## schedule

* [x] 0 2019/09/11
* [ ] 1 2019/09/14
