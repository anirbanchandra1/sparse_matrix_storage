'''
Two types of input matrices can be created
1) Hardcoded matrix - User inputs all elements: hard_code_matrix()
2) Create a random matrix with certain random elements zeroed out 
    - User inputs matrix elements the number of zeros they want in 
    the matrix: create_sparse_matrix()
'''

'''
# a Hardcoded matix 
def hard_code_matrix():
    T_mat = [[1, 2, 6, 8, 0], 
             [3, 4, 0, 0, 9],
             [1, 0, 0, 0, 2], 
             [7, 2, 0, 3, 1], 
             [4, 0, 6, 0, 2]]
    return T_mat
'''

# another Hardcoded matix 
def hard_code_matrix():
    T_mat = [[1, 2, 6, 1, 0, 2], 
             [4, 3, 0, 0, 1, 3],
             [1, 0, 3, 0, 2, 0], 
             [4, 2, 1, 0, 1, 0], 
             [4, 0, 6, 0, 2, 0]]
    return T_mat



## ADDITIONAL TEST CASE
# Random matrix with num_zeros '0.0' elements
# not super robust, but can be used for additional testing
# Note: uses numpy for creating random elements
import numpy as np
def create_sparse_matrix(num_rows, num_cols, num_zeros):
    T_mat = np.random.rand(num_rows,num_cols)*100.
    i = 0
    while i < num_zeros:            
        irow = np.random.randint(num_rows)
        icol = np.random.randint(num_cols)
        if T_mat[irow, icol] != 0.:
            T_mat[irow, icol] = 0.
        else:
            i-=1
        i+=1
        print(i)
    return T_mat





