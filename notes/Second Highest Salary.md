---
tags: [2019/11/03, leetcode/176]
title: Second Highest Salary
created: '2019-09-24T14:50:29.836Z'
modified: '2019-10-27T04:23:00.238Z'
---

# Second Highest Salary

Write a SQL query to get the second highest salary from the Employee table.

```
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```

For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

```
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```

## Solution

```sql
# Write your MySQL query statement below

SELECT (
SELECT DISTINCT
    Salary
FROM
    Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1 ) AS SecondHighestSalary;
```

```sql
# Write your MySQL query statement below


SELECT 
    IFNULL (
        (
            SELECT DISTINCT
                Salary
            FROM Employee
            ORDER BY Salary DESC
            LIMIT 1 OFFSET 1
        ), 
        NULL
    )
AS SecondHighestSalary;
```

## schedule

* [x] 0 2019/09/26
* [x] 1 2019/09/27
* [x] 1 2019/09/28
* [x] 1 2019/10/01
* [x] 1 2019/10/08
* [x] 1 2019/10/23
* [x] 1 2019/10/24
* [x] 1 2019/10/27
* [ ] 1 2019/11/03
