# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 14:05:01 2019

@author: jortiz
@Homework Assignment: #3 If Statements
"""

#if conditon:
#    Action

def ifHomework(a,b,c):
    bolVariable = False
    if(int(a) == int(b) or int(a) == int(c) or int(b) == int(c)):
        bolVariable = True
        print(bolVariable)
        
    else:
        print(bolVariable)
        
ifHomework(1,3,"2")