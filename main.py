from sparse_matrix import sparse_matrix
from create_T_matrix import hard_code_matrix 
# if additional test cases are necessary use the "create_sparse_matrix" function below
from create_T_matrix import create_sparse_matrix


# Function for calculating the heat flux (T_grad) of a given temperature field (T_mat) 
# note that the gradient is taken along the columns
# T_grad is a sparse_matrix object
def calc_gradient_sparse(T_mat, T_grad, num_rows, num_cols, k, dx):
    for irow in range(num_rows-2): # loop over rows of gradient matrix
        for jcol in range(num_cols-2): # loop over columns of gradient matrix
            grad_val = -k*(T_mat[irow+2][jcol+1] - T_mat[irow][jcol+1])/2./dx # calculate the value of gradient
            T_grad.assign(irow, jcol, grad_val) # Store the gradient value sparsely

if __name__ == '__main__':
    ## -- User Inputs -- ##
    n = 6 # num cols
    m = 5 # num rows
    k = 3 # thermal conductivity
    dx = 0.2 # grid spacing

    # Get the user input matrix
    T_mat = hard_code_matrix()
    
    # If creating random matrix with certain number of zeroes
    #o = 10 # number of zeros in the matrix
    #T_mat = create_sparse_matrix(n, m, o)
    
    print('Input Matrix:\n', T_mat)
    
    # Initialize the spare_matrix object for storing the gradient of T_mat matrix
    T_grad = sparse_matrix(m-2,n-2)
    
    # Calculate the gradient matrix
    calc_gradient_sparse(T_mat, T_grad, m, n, k, dx)
    
    print('Sparsely stored gradient matrix:\n', [[T_grad.arr_ind[i], T_grad.arr_val[i]] for i in range(len(T_grad.arr_ind))])
    print('Gradient matrix (full representation):\n', [[T_grad.extract(i,j) for j in range (n-2)] for i in range(m-2)])
