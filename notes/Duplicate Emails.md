---
tags: [2019/10/20, leetcode/182]
title: Duplicate Emails
created: '2019-09-22T11:17:34.233Z'
modified: '2019-10-06T10:49:46.970Z'
---

# Duplicate Emails

Write a SQL query to find all duplicate emails in a table named Person.
```
+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
```

For example, your query should return the following for the above table:

```
+---------+
| Email   |
+---------+
| a@b.com |
+---------+


```
Note: All emails are in lowercase.

## Solution

```sql
# Write your MySQL query statement below



select
    Email
From (
select 
    Email, count(Id) as cnt
from
    Person
group by Email
) as tmp
where cnt > 1;

```

## schedule

* [x] 0 2019/09/24
* [x] 1 2019/09/25
* [x] 1 2019/09/28
* [x] 1 2019/10/05
* [ ] 1 2019/10/20
