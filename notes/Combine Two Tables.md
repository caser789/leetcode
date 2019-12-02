---
tags: [2019/11/02, leetcode/175]
title: Combine Two Tables
created: '2019-09-24T14:49:25.684Z'
modified: '2019-10-26T14:59:59.565Z'
---

# Combine Two Tables

Table: Person

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
```

PersonId is the primary key column for this table.
Table: Address

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
```

AddressId is the primary key column for this table.
 

Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:

FirstName, LastName, City, State


## Solution

```sql
# Write your MySQL query statement below

Select 
    FirstName, LastName, City, State
FROM
    Person left JOIN Address
ON
    Person.PersonId = Address.PersonId
;
```

## schedule

* [x] 0 2019/09/26
* [x] 1 2019/09/27
* [x] 1 2019/09/30
* [x] 1 2019/10/07
* [x] 1 2019/10/22
* [x] 1 2019/10/23
* [x] 1 2019/10/26
* [ ] 1 2019/11/02
