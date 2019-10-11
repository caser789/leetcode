---
tags: [2019/10/22, leetcode/183, sql]
title: Customers Who Never Order
created: '2019-09-24T14:52:09.644Z'
modified: '2019-10-08T04:55:06.256Z'
---

# Customers Who Never Order

Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

Table: Customers.

```
+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
```

Table: Orders.

```
+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
```

Using the above tables as example, return the following:

```
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
```

## Solution

```sql
# Write your MySQL query statement below


select
    Name AS Customers
from
    Customers
where
    Id not in (select CustomerId from orders);
```

## schedule

* [x] 0 2019/09/26
* [x] 1 2019/09/27
* [x] 1 2019/09/30
* [x] 1 2019/10/07
* [ ] 1 2019/10/22
