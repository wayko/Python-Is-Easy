# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 13:08:16 2019

@author: jortiz
"""

myUniqueList = []
myLeftOvers = []
 

def addToList(addItem):
    seen = set(myUniqueList)
    if addItem not in seen:
        seen.add(addItem)
        myUniqueList.append(addItem)
    else:
        print(str)
        rejectedItem(addItem)
       
def rejectedItem(rejectedItem):
    myLeftOvers.append(rejectedItem)
    
addToList(1)
addToList(2)
addToList(3)
addToList(3)
addToList(4)
addToList(2)
print(myUniqueList)
print(myLeftOvers)