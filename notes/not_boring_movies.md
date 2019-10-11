---
tags: [2019/10/11, leetcode/620, sql]
title: Not Boring Movies
created: '2019-09-24T15:22:54.634Z'
modified: '2019-10-05T05:04:30.854Z'
---

# Not Boring Movies

X city opened a new cinema, many people would like to go to this cinema. The cinema also gives out a poster indicating the movies’ ratings and descriptions.
Please write a SQL query to output movies with an odd numbered ID and a description that is not 'boring'. Order the result by rating.

 

For example, table cinema:

```
+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   1     | War       |   great 3D   |   8.9     |
|   2     | Science   |   fiction    |   8.5     |
|   3     | irish     |   boring     |   6.2     |
|   4     | Ice song  |   Fantacy    |   8.6     |
|   5     | House card|   Interesting|   9.1     |
+---------+-----------+--------------+-----------+
For the example above, the output should be:
+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   5     | House card|   Interesting|   9.1     |
|   1     | War       |   great 3D   |   8.9     |
+---------+-----------+--------------+-----------+
```

## Solution

```sql
# Write your MySQL query statement below

select
    *
from
    cinema
where 
    description != 'boring' AND
    mod(id, 2) = 1
order by
    rating
desc
;


```


## schedule

* [x] 0 2019/09/30
* [x] 1 2019/10/01
* [x] 1 2019/10/04
* [ ] 1 2019/10/11
