# -*- coding: utf-8 -*-
"""
Created on Mon May 30 22:01:23 2022

@author: cauli

messing with lists
"""
import string
import random

def rand_string_func(length_word):  
    rand_string = "" 
    for i in range(length_word):
        rand_choice = random.choice(string.ascii_lowercase)
        rand_string += rand_choice 
    return rand_string

def unsorted_list_func(length_list, length_word):
    list_1 = []
    for i in range(length_list):
        list_1.append(rand_string_func(length_word))
    return list_1

def list_sorter_func(unsorted_list):
    unsorted_list.sort()
    sorted_list = unsorted_list
    return sorted_list

var_unsorted_list = unsorted_list_func(5,3)

var_sorted_list = list_sorter_func(var_unsorted_list)
  
print(var_unsorted_list)
print(var_sorted_list)
