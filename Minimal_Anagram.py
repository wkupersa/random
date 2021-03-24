#!/bin/env python
'''
Given two equal-size strings s and t. In one step you can choose any 
character of t and replace it with another character.
Return the minimum number of steps to make t an anagram of s.
An Anagram of a string is a string that contains the same characters 
with a different (or the same) ordering.
'''

class Solution:
    def minSteps(self, s: str, t: str) -> int:

        t = list(t)

        for i in s:
            if i in t:
                t.remove(i)
        return(len(t))





test = Solution()

import random
s = ""
t = ""
for i in range(1,200000):
    s += chr(random.randint(97,120))
    t += chr(random.randint(97,120))

print(s)
print(t)
print(test.minSteps(s,t))
