# -*- coding: utf-8 -*-
"""
Created on Mon May 30 22:51:45 2022

@author: cauli

Given a positive integer A, return an array of strings with all the integers
from 1 to N. 
But for multiples of 3 the array should have “Fizz” instead of the number. 
For the multiples of 5, the array should have “Buzz” instead of the number. 
For numbers which are multiple of 3 and 5 both, the array should have “FizzBuzz”
instead of the number.

"""
#string_N = input("Please enter the number of iterations: ")
string_N = 15
int_1 = 3
int_2 = 5

int_N= int(string_N)
word_1 = "Fizz"
word_2 = "Buzz"

for i in range(int_N):
    count = i+1
    
    if count%int_2==0 and count%int_1==0:
        print(word_1+word_2)
        break
    if count%int_1 ==0:
        print(word_1)
    if count%int_2==0:
        print(word_2)
    
    else:
        print(count)
