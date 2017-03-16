# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 10:33:16 2016

@author: Abhishek
"""

import fileinput
f = fileinput.input()

def word(a):
    p=list(set(a))
    return len(p)


t = int(raw_input())
n=int(raw_input())
for i in range(t):
    s=[]
    nam=[]
    for j in range (n):
       try: 
        a = raw_input().strip()
       except EOFError:
           fdfd=0
       nam=nam+[a]
       s=s+[word(a)]
    mz=max(s)
    print "Case #{}: {}".format(i+1, nam[s.index(mz)])