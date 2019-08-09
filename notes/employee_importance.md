---
tags: [2019/08/07, data structure/queue, data structure/tree, leetcode/690, method/traversal/bfs]
title: Employee Importance
created: '2019-08-07T05:38:02.816Z'
modified: '2019-08-09T04:45:19.074Z'
---

# Employee Importance

You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.

### Example 1:

```
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation: Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
```



> One employee has at most one direct leader and may have several subordinates.
> The maximum number of employees won't exceed 2000.


```python
"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        store = {}
        for employee in employees:
            store[employee.id] = employee
        if id not in store:
            return 0
        q = [id]
        res = 0
        while q:
            next_q = []
            for _id in q:
                node = store[_id]
                res += node.importance
                next_q.extend(node.subordinates)
            q = next_q
        return res
```
