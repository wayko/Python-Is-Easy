# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:28:50 2019

@author: jortiz
@title: Intro to Loops
"""

Word = "Hello"

for letters in Word:
    print(letters)

counter = 1
Sum = 0    
while (counter <= 100):
    print(counter)
    Sum = Sum + counter
    counter += 1
print(Sum)
    