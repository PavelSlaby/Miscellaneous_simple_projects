'''
SUDOKU Algorithm

The algorithm goes cell by cell throught the whole sudoku matrix. 
At each "null cell", it performs first one algorithm (denoted as ALGORITHM 1) and then a second one (denoted as ALGORITHM 2)

ALGORITHM 1: 
    Algorithm finds all the possible numbers that could be filled in the cell, 
    given the already filled in numbers in respective row, column and submatrix. 
    If there is only one option, the algortihm will fill it in and start again at the next empty cell.  
    If there are more options the algortihm will move to ALGORITHM 2
    
ALGORITHM 2:
    If the the current cell is still empty after performing ALGORITHM 1, the ALGORITHM 2 will be applied.
    This algoithm realizes that each column has to contain all the numbers (1-9) exactly ones. 
    So it takes the possible numbers that could be filled in from ALGORITHM 1 (options set) and then it looks one by one 
    at all these options. For each number it chcecks all the empty cells in the respective column. 
    At each respective cell in the columnn it checks, whether the particular number could be filled in. 
    If a number could be filled in more of the cells of the respective column, it is disqualified. If after thsi disqualifieng round, 
    only one option is left, than this number is actually filled in.
    
ALGORITHM 3:
    Is the same as ALGORITHM 2, but it looks at rows instead of columns.    
    
This is reapeted until the last cell in the matrix. 
The whole process is then repeated until there are no more cells with zeros or until it reaches certain number of repetitions.

the algorithm is quite simple, it can not however solve the most difficult types of sudoku everytime. 
There is a need to implement one more algorithm. Improvement of the algorithm is in process.....
'''
#%% Sudoku Loader 
import pandas as pd
import numpy as np
import os 

os.getcwd()
os.chdir('F:\_Python\misc projects\Sudoku')

# The Sudoku can be declared either via:
# 1] Numpy array
sudoku = np.array([
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

# 2] Import from excel file
file = 'sudoku.xlsx'
raw = pd.read_excel(file, header = None, sheet_name = 'Hard')
sudoku = np.nan_to_num(np.asarray(raw))

#%% necessary declarations
def upper_bound(x): #function defines the upper boundary of a sub-matrix     
    for k in [3, 6, 9]:
        if x < k:
            return k 

possibles = {1,2, 3, 4, 5, 6, 7, 8, 9} #set of all generaly possible numbers to be filled in, 0 is not one of them

mat = sudoku.copy()

#%% Computing logic

p = 0
while np.min(mat) == 0: # appplies the algorithm as long as the matrix contains zeros
        p += 1 
        if p > 350: 
            raise TypeError("Finished" + str(p-1) +"th cycle, the algorithm will stop now")
            break #break so that the cycle does not go on forever, if sudoku unsolvable          
        for i in range(0, 9): #over rows
            for j in range(0, 9): #over columns  
                if mat[i, j] == 0:         
                    # ALGORITHM 1 - looking at respective row/column/submatrix
                    row_ops = possibles - set(mat[i])
                    col_ops = row_ops - set(mat[:,j])
                    m = upper_bound(i)
                    n = upper_bound(j)
                    options = col_ops - set(mat[(m-3):m, (n-3):n].flatten()) #all numbers that could possibly be filled in the cell
                    if len(options) ==  1: 
                        mat[i, j] = int(list(options)[0])
                    # ALGORITHM 2 - checks if the number could be anywhere else in the respective column
                    else:
                        unsuitable = set() #list of numbers that we can rule out
                        for o in list(options): # options - list of all the numbers that could be possibly filled in
                            o = {o}
                            col = j
                            row = i
                            for row in range(0, 9): # goes row by row
                                if mat[row, col] == 0: 
                                    t = upper_bound(col)
                                    s = upper_bound(row)
                                    if row == i and o not in set(mat[(s-3):s, (t-3):t].flatten()).union(set(mat[row,:])):
                                        pass # it is ok, if the o is not anywhere in its respective row or submatrix
                                    elif row != i and o.intersection(set(mat[(s-3):s, (t-3):t].flatten()).union(set(mat[row,:]))) == o:
                                        pass # it is ok, if the o is somewhere in its respective row or submatrix, checking each row
                                    else:
                                        unsuitable = unsuitable.union(o) # all else would disqualify o                                    
                        if len(options - unsuitable) == 1: # if there is only one option left, it is filled in
                           mat[i, j] = int(list(options - unsuitable)[0])
                  # ALGORITHM 3 - same like algorithm 2, but it checks the respective row
                        else:
                            unsuitable2 = set()
                            for o in list(options): 
                                o = {o}
                                col = j
                                row = i
                                for col in range(0, 9): 
                                    if mat[row, col] == 0: 
                                        t = upper_bound(col)
                                        s = upper_bound(row)
                                        if col  == j and o not in set(mat[(s-3):s, (t-3):t].flatten()).union(set(mat[:,col])):
                                            pass 
                                        elif col != j and o.intersection(set(mat[(s-3):s, (t-3):t].flatten()).union(set(mat[:,col]))) == o:
                                            pass 
                                        else:
                                            unsuitable2 = unsuitable2.union(o)                                   
                            if len(options - unsuitable2) == 1: 
                               mat[i, j] = int(list(options - unsuitable2)[0])
print(mat)


         
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        unsuitable2 = set()
                        for o in list(options):
                            o = {o}
                            col2 = j
                            row2 = i
                            for col2 in range(0, 9): # goes row by row, each row has to contain all numbers, this checks whether a particular number could be filled in in any other cell in the same number, if not, it has to be filled in in current cell
                                if mat[row2, col2] == 0: 
                                    t = upper_bound(col2)
                                    s = upper_bound(row2)
                                    if col2 == j and o not in set(mat[(s-3):s, (t-3):t].flatten()).union(set(mat[col2])):
                                        pass
                                    elif col2 != j and o.intersection(set(mat[(s-3):s, (t-3):t].flatten()).union(set(mat[col2]))) == o:
                                        pass
                                    else:
                                        unsuitable2 = unsuitable2.union(o)
                        if len(options - unsuitable2) == 1:
                            mat[i, j] = int(list(options - unsuitable2)[0])
                        else:
                            pass
                           




