---
tags: [2019/11/22, bash, leetcode/193]
title: Valid Phone Numbers
created: '2019-09-24T14:55:22.719Z'
modified: '2019-10-22T05:20:28.977Z'
---

# Valid Phone Numbers

Given a text file file.txt that contains list of phone numbers (one per line), write a one liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.

### Example:

Assume that file.txt has the following content:

987-123-4567
123 456 7890
(123) 456-7890
Your script should output the following valid phone numbers:

987-123-4567
(123) 456-7890

## Solution

```
# Read from the file file.txt and output all valid phone numbers to stdout.

grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt  # Pattern

grep -P '^\d{3}-\d{3}-\d{4}$' file.txt
grep -P '\(\d{3}\) \d{3}-\d{4}$' file.txt

```

## schedule

* [x] 0 2019/09/26
* [x] 1 2019/09/27
* [x] 1 2019/09/30
* [x] 1 2019/10/07
* [x] 1 2019/10/22
* [ ] 1 2019/11/22
