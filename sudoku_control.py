'''
Checks if there is any error in the Sudoku. 
The algorithm first checks if there are any duplicate numbers in a row, column and submatrix.

'''

def wo_zeros(matrix): #drops zeros out of the array
    return np.delete(matrix, np.where(matrix ==0))

def sudoku_control(matrix):
    # matrix must be numpy.ndarray type, filled in with numbers 0 - 10, with 0 indicating "empty" cell 
    k = []
    l = []
    
    for i in range(0,9): #checks rows
        if len(wo_zeros(matrix[i, :])) != len(set(matrix[i, :]) - {0}):
           k.append(i + 1)
    
    for j in range(0,9): #checks columns
        if len(wo_zeros(matrix[:, j]))!= len(set(matrix[:, j]) - {0}):
            l.append(j + 1)
    
    submatrix = []
    boundaries = [3, 6, 9]
    for m in boundaries: #checks submatrixes
        for n in boundaries:
            if len(wo_zeros(matrix[m-3:m, n-3:n].flatten())) != len(set(matrix[m-3:m, n-3:n].flatten()) - {0}):
                submatrix.append(str(m-3) + ":" + str(m) +"," + str(n-3) + ":" + str(n))            
    
    if len(k + l + submatrix) !=0:
        print("There is a problem in row " + str(k) + " column " + str(l) + " and submatrix " + str(submatrix) )
    elif np.min(matrix) != 0 and len(k + l + submatrix) == 0:
        print("Sudoku is completely filled in and no problem detected, Congrats!")   
    else: 
        print("No problem detected, but Sudoku is not complete")


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


sudoku_control(sudoku)


