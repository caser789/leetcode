---
tags: [2019/11/22, leetcode/196, sql]
title: Delete Duplicate Emails
created: '2019-09-24T14:57:44.304Z'
modified: '2019-10-22T05:15:22.702Z'
---

# Delete Duplicate Emails

Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.

```
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
```
Id is the primary key column for this table.
For example, after running your query, the above Person table should have the following rows:

```
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
```

Note:

Your output is the whole Person table after executing your sql. Use delete statement.

## Solution

```sql
# Write your MySQL query statement below

DELETE p1 
FROM Person p1, Person p2
WHERE
    p1.Email = p2.Email AND
    p1.Id > p2.Id;
```

## schedule

* [x] 0 2019/09/26
* [x] 1 2019/09/27
* [x] 1 2019/09/30
* [x] 1 2019/10/07
* [x] 1 2019/10/22
* [ ] 1 2019/11/22
