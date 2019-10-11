---
tags: [2019/10/11, leetcode/195]
title: Tenth Line
created: '2019-09-24T14:56:42.616Z'
modified: '2019-10-09T14:11:36.979Z'
---

# Tenth Line

Given a text file file.txt, print just the 10th line of the file.

Example:

Assume that file.txt has the following content:

Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
Your script should output the tenth line, which is:

Line 10
Note:
1. If the file contains less than 10 lines, what should you output?
2. There's at least three different solutions. Try to explore all possibilities.

## Solution

```sh
# Read from the file file.txt and output the tenth line to stdout.

# Solution 2
awk 'FNR == 10 {print }'  file.txt
# OR
awk 'NR == 10' file.txt

# Solution 3
sed -n 10p file.txt

# Solution 4
tail -n+10 file.txt|head -1
```


## schedule

* [x] 0 2019/09/26
* [x] 1 2019/09/27
* [x] 1 2019/09/30
* [x] 1 2019/10/07
* [x] 1 2019/10/08
* [ ] 1 2019/10/11
