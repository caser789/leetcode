---
tags: [2019/10/28, leetcode/929]
title: Unique Email Addresses
created: '2019-08-31T08:42:21.188Z'
modified: '2019-09-26T15:43:04.034Z'
---

# Unique Email Addresses

Every email consists of a local name and a domain name, separated by the @ sign.

For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails?


### Example 1:

Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails


> 1 <= emails[i].length <= 100
> 1 <= emails.length <= 100
> Each emails[i] contains exactly one '@' character.
> All local and domain names are non-empty.
> Local names do not start with a '+' character.

## Solution

```python
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        addr = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.split('+')[0]
            local_name = ''.join(local_name.split('.'))
            addr.add('@'.join([local_name, domain_name]))
        return len(addr)
```

## schedule

* [x] 0 2019/09/01
* [x] 1 2019/09/02
* [x] 3 2019/09/05
* [x] 3 2019/09/12
* [x] 3 2019/09/27
* [ ] 3 2019/10/28

