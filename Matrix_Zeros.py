# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 11:20:01 2022

@author: Kaitlin

Objective: to construct a function that for every element that equals 0 
the corresponding row and column will be overwritten as zero
"""
import numpy as np
import math

def matzero(mat):
    n, m = mat.shape # getting matrix dimensions n = row, m = column
    ind = m*n # number of indices in array to make one for loop
    x = np.array([]) # to store locations that equal zero
    
    for i in range(0,ind): # loop over matrix to find zeros
        j = math.floor(i / m)
        k = i % m
        if mat[j,k] == 0:
            x = np.append(x,i)
            print(x)
    
    for i in x: # adding zeros to the corresponding rows and columns
        j = int(math.floor(i / m))
        k = int(i % m)
        mat[:,k] = 0
        mat[j,:] = 0
    return mat

mat = np.array([[2, 0, 7], [3, 5, 6], [5, 9, 0]]) # example case
print(matzero(mat))
