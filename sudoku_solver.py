# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 10:09:05 2020

@author: pavel_000
"""
'''
EASY - SUDOKU Algorithm

The algorithm goes cell by cell throught the whole sudoku matrix. At each "null cell", it looks at all the possible numbers
that could be filled in, given the already filled in cells in respective row, column and submatrix. 
If there is only one option, the algortihm will fill it in. If there are more options the algortihm will move to the next cell.
This is reapeted until the last cell in the matrix. 
The whole process is then repeated until there are no more cells with zeros.

- the algorithm is quite simple, it can not however solve all types of sudokus - pretty much only the simple ones.
Improvement of the algorithm is in process.....
'''

expert = np.array([
        [1,2,0,6,0,8,0,0,9],
        [7,0,0,0,0,1,5,0,0],    
        [5,0,0,0,0,0,0,0,2],
        [0,0,0,0,0,2,3,4,5], 
        [0,9,0,0,1,0,0,0,6],
        [0,0,5,0,0,7,0,0,0],     
        [0,7,0,0,0,0,9,1,0],
        [0,0,0,3,0,0,0,0,0], 
        [6,0,0,0,0,0,0,0,0]
        ])



final = mat.copy()

# Sudoku solver

import pandas as pd
import numpy as np
import os 

os.getcwd()
os.chdir('F:\_Python\misc projects\Sudoku')

file = 'sudoku.xlsx'

raw = pd.read_excel(file, header = None)
np_raw = np.nan_to_num(np.asarray(raw))

original = np_raw.copy()

mat = np_raw.copy()

def upper_bound(x): #defines the upper boundary of a sub-matrix     
    for k in [3, 6, 9]:
        if x < k:
            return k 

possibles = {1,2, 3, 4, 5, 6, 7, 8, 9} #set of all generaly possible numbers to be filled in, 0 is not one of them

mat = np_raw.copy()
mat = expert.copy() 
p = 0
while np.min(mat) == 0: # appplies the algortihm as long as the matrix containts zeros
        p += 1 
        if p >= 150: break #break so that the cycle does not go on forever, if sudoku unsolvable        
        for i in range(0, 9): #over rows
            for j in range(0, 9): #over columns  
                if mat[i, j] == 0:         
                    row = possibles - set(mat[i])
                    col = row - set(mat[:,j])
                    m = upper_bound(i)
                    n = upper_bound(j)
                    options = col - set(mat[(m-3):m, (n-3):n].flatten()) #all numbers that could possibly be filled in the cell
                    if len(options) ==  1: 
                        mat[i, j] = int(list(options)[0])
                    else:
                        for o in list(options):
                            consider = []
                            o = {o}
                            col = j
                            row = i
                            for col in range(0, 9): # goes column by column
                                if mat[row, col] == 0:
                                    t = upper_bound(col)
                                    s = upper_bound(row)
                                    if o.intersection(set(mat[(s-3):s, (t-3):t].flatten())) == set() and o.intersection(set(mat[:, col])) == set():
                                        consider.append(int(list(o)[0]))
                                    else:
                                        pass
                            # if len(consider) == 1:
                            #    mat[i, j] = consider[0] #insert break
                            # col = j
                            # consider = []
                            # for row in range(0, 9): # goes row by row
                            #            if mat[row, col] == 0:
                            #                t = upper_bound(col)
                            #                s = upper_bound(row)
                            #                if o.intersection(set(mat[(s-3):s, (t-3):t].flatten())) == set() and o.intersection(set(mat[row,:])) == set():
                            #                    consider.append(int(list(o)[0]))
                            #                else:
                            #                    pass
                            # if len(consider) == 1:
                            #    mat[i, j] = consider[0]
                    
options = [1, 6, 7, 8]
i = 3
j = 2
o = {7}

col = j
row = i
for col in range(0, 9): # goes column by column
    if mat[row, col] == 0:
        t = upper_bound(col)
        s = upper_bound(row)
        consider = []
        if o.intersection(set(mat[:, col]), set(mat[(s-3):s, (t-3):t].flatten())) == set():
            consider.append(int(list(o)[0]))
        else:
            pass
if len(consider) == 1:
    mat[i, j] = consider[0]

      
for o in list(options):
    o = {o}


        
mat
mat[i, j]
submat

{7}.intersection({7})
a = set(mat[(s-3):s, (t-3):t].flatten())
b = set(mat[:, col])
o.intersection(b).intersection(a)
