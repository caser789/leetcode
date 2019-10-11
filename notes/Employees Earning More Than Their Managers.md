---
tags: [2019/10/22, leetcode/181]
title: Employees Earning More Than Their Managers
created: '2019-09-24T14:51:22.006Z'
modified: '2019-10-08T05:07:15.026Z'
---

# Employees Earning More Than Their Managers

The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

```
+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
```

Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

```
+----------+
| Employee |
+----------+
| Joe      |
+----------+
```

## Solution

```sql
# Write your MySQL query statement below


SELECT
    a.NAME as 'Employee'
FROM
    Employee AS a,
    Employee As b
WHERE
    a.ManagerId = b.Id AND
    a.Salary > b.Salary
;

```

```sql
# Write your MySQL query statement below

SELECT
    a.NAME AS Employee
FROM Employee AS a JOIN Employee AS b
ON a.ManagerId = b.Id AND
    a.Salary > b.Salary
    ;
```

## schedule

* [x] 0 2019/09/26
* [x] 1 2019/09/27
* [x] 1 2019/09/30
* [x] 1 2019/10/07
* [ ] 1 2019/10/22
