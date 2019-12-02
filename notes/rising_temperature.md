---
tags: [2019/11/23, leetcode/197, sql]
title: Rising Temperature
created: '2019-09-24T14:59:13.339Z'
modified: '2019-10-23T04:40:15.605Z'
---

# Rising Temperature

Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.

```
+---------+------------------+------------------+
| Id(INT) | RecordDate(DATE) | Temperature(INT) |
+---------+------------------+------------------+
|       1 |       2015-01-01 |               10 |
|       2 |       2015-01-02 |               25 |
|       3 |       2015-01-03 |               20 |
|       4 |       2015-01-04 |               30 |
+---------+------------------+------------------+
```

For example, return the following Ids for the above Weather table:

```
+----+
| Id |
+----+
|  2 |
|  4 |
+----+
```

## Solution

```
# Write your MySQL query statement below

select
    b.Id
from
    Weather a, Weather b
where
    datediff(b.RecordDate, a.RecordDate) = 1 AND
    b.Temperature > a.Temperature
    ;
```

```sql
# Write your MySQL query statement below

select
    b.Id
from
    Weather a join Weather b
on
    datediff(b.RecordDate, a.RecordDate) = 1 AND
    b.Temperature > a.Temperature
;
```

## schedule

* [x] 0 2019/09/27
* [x] 1 2019/09/28
* [x] 1 2019/10/01
* [x] 1 2019/10/08
* [x] 1 2019/10/23
* [ ] 1 2019/11/23
