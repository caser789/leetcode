---
favorited: true
tags: [2019/11/03, data structure/priority queue, leetcode/295]
title: Find Median from Data StreamFind Median from Data Stream
created: '2019-10-19T03:28:32.706Z'
modified: '2019-10-27T06:08:42.897Z'
---

# Find Median from Data StreamFind Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

### Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

## Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

## Solution

### sort when find

```python
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []
        self.n = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.values.append(num)
        self.n += 1

    def findMedian(self):
        """
        :rtype: float
        """
        if self.n == 0:
            return float(0)

        self.values.sort()
        m = self.n / 2
        if self.n % 2 == 1:
            return 1.0 * self.values[m]
        return 1.0 * (self.values[m-1] + self.values[m]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

```

### sort when insert

```python
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []
        self.n = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.values:
            self.values.append(num)
        else:
            j = find(self.values, 0, self.n, num)
            self.values.append(None)
            k = self.n
            while k > j:
                self.values[k] = self.values[k-1]
                k -= 1
            self.values[k] = num
        self.n += 1

    def findMedian(self):
        """
        :rtype: float
        """
        if self.n == 0:
            return float(0)

        m = self.n / 2
        if self.n % 2 == 1:
            return 1.0 * self.values[m]
        return 1.0 * (self.values[m-1] + self.values[m]) / 2


def find(lst, i, j, v):
    while i < j:
        mi = (i+j) / 2
        if lst[mi] <= v:
            i = mi + 1
        else:
            j = mi
    return i


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


```

### heap

```
import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.hi = []
        self.lo = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.lo) > len(self.hi):
            return - 1.0 * self.lo[0]
        return 0.5 * (self.hi[0] - self.lo[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```



## schedule

* [x] 0 2019/10/19
* [x] 1 2019/10/20
* [x] 1 2019/10/24
* [x] 1 2019/10/27
* [ ] 1 2019/11/03

