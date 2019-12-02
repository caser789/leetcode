---
tags: [2019/11/19, leetcode/627]
title: Swap Salary
created: '2019-09-22T11:05:42.070Z'
modified: '2019-10-19T13:26:58.064Z'
---

# Swap Salary

Given a table salary, such as the one below, that has m=male and f=female values. Swap all f and m values (i.e., change all f values to m and vice versa) with a single update statement and no intermediate temp table.

Note that you must write a single update statement, DO NOT write any select statement for this problem.



Example:

| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
After running your update statement, the above salary table should have the following rows:
| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | f   | 2500   |
| 2  | B    | m   | 1500   |
| 3  | C    | f   | 5500   |
| 4  | D    | m   | 500    |

## Solution

```
# Write your MySQL query statement below

UPDATE salary
SET
    sex =
        CASE sex
            WHEN 'f' THEN 'm'
            ELSE 'f'
        END;
```

## schedule

* [x] 0 2019/09/23
* [x] 1 2019/09/24
* [x] 1 2019/09/27
* [x] 1 2019/10/04
* [x] 1 2019/10/19
* [ ] 1 2019/11/19
