---
tags: [2020/01/03, leetcode/721, method/union find]
title: Accounts Merge
created: '2019-08-11T11:17:53.969Z'
modified: '2020-01-02T15:08:29.459Z'
---

# Accounts Merge

Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

### Example 1:

```
Input:
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation:
    The first and third John's are the same person as they have the common email "johnsmith@mail.com".
    The second John and Mary are different people as none of their email addresses are used by other accounts.
    We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
    ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
```

> The length of accounts will be in the range [1, 1000].
> The length of accounts[i] will be in the range [1, 10].
> The length of accounts[i][j] will be in the range [1, 30].

## Solution

```python
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        
        [
            ["John", "johnsmith@mail.com", "john00@mail.com"], 
            ["John", "johnnybravo@mail.com"], 
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
            ["Mary", "mary@mail.com"],
        ]
        """
        index = 0
        email_to_index = {}
        email_to_name = {}
        
        uf = UF(10001)
        
        for lst in accounts:
            name = lst[0]
            for i in range(1, len(lst)):
                email = lst[i]
                email_to_name[email] = name
                if email not in email_to_index:
                    email_to_index[email] = index
                    index += 1
                    
                
                uf.union(email_to_index[lst[1]], email_to_index[lst[i]])
                    
        root_to_emails = {}
        for email in email_to_name:
            i = email_to_index[email]
            root = uf.find(i)
            root_to_emails.setdefault(root, [])
            root_to_emails[root].append(email)
        
        res = []
        for _, emails in root_to_emails.items():
            name = email_to_name[emails[0]]
            res.append([name] + sorted(emails))
        
        return res
        
        
        
class UF(object):
    def __init__(self, n):
        self.n = n
        self.parents = range(n)
        self.ranks = [0] * n
    
    def __len__(self):
        return self.n
    
    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p
    
    def union(self, p, q):
        u = self.find(p)
        v = self.find(q)
        if u == v:
            return
        
        if self.ranks[u] < self.ranks[v]:
            self.parents[u] = v
        elif self.ranks[u] > self.ranks[v]:
            self.parents[v] = u
        else:
            self.parents[u] = v
            self.ranks[v] += 1
        self.n -= 1
        
```

## schedule

* [x] 2020/01/02
* [ ] 2020/01/03

## refs

* [lc](https://leetcode.com/problems/accounts-merge/)
