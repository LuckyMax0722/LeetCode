class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        import numpy as np
        matrix_np = np.array(matrix)
        return (matrix_np.T).tolist()
        '''

        transposed_list = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        return transposed_list