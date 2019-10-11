---
tags: [2019/10/11, leetcode/596, sql]
title: Classes More Than 5 Students
created: '2019-09-17T15:34:06.328Z'
modified: '2019-09-26T04:54:35.487Z'
---

# Classes More Than 5 Students

There is a table courses with columns: student and class

Please list out all classes which have more than or equal to 5 students.

For example, the table:

```
+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+
```
Should output:

```
+---------+
| class   |
+---------+
| Math    |
+---------+
```


## Note:

The students should not be counted duplicate in each course.

# Write your MySQL query statement below

## group by

```sql
SELECT
    class
FROM
    courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5
;
```


## schedule

* [x] 0 2019/09/15
* [x] 1 2019/09/16
* [x] 1 2019/09/19
* [x] 1 2019/09/26
* [ ] 1 2019/10/11
