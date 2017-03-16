# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 02:29:53 2016

@author: Abhishek
"""

txt = "AABAACAADAABAAABAA"
pat = "AABA"
p=len(pat)
t=len(txt)
for i in range (t-p+1):
    if(txt[i:p+i] == pat):
        print i