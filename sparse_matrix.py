# Sparse matrix class definition

class sparse_matrix:
    '''sparse matrix class'''
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.arr_ind = []
        self.arr_val = []
        
    ''' assign() method stores the sparse matrix'''
    @staticmethod
    def get_sparse_index(col,i,j):
        return i*col + j
    
    def assign(self, i, j, dVal):
        #if abs(dVal) <= 1e-12 : dVal = 0.0
        #if dVal == 0.0:
        if abs(dVal) <= 1e-12:
            pass
        else:
            #self.arr_red.append([i*self.col + j, dVal])
            self.arr_ind.append(self.get_sparse_index(self.col,i,j))
            self.arr_val.append(dVal)

    ''' extract() method queries a particular index and returns the 
        value of the actual matrix, i.e., it will return zeroes too'''
    def extract(self, i,j):
        #index_list = [row[0] for row in self.arr_red]     
        try:
            #ind = index_list.index(i*self.col + j)
            #ind = index_list.index(self.get_sparse_index(self.col,i,j))
            ind  = self.arr_ind.index(self.get_sparse_index(self.col,i,j))
            return self.arr_val[ind]
        except ValueError:
            return 0.0

