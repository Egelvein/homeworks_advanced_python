class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, m2):
        if self.rows != m2.rows or self.cols != m2.cols:
            raise ValueError('Matrices must have same shapes for addition')

        m_result = []

        for i in range(self.rows):
            row_m_result = []
            for j in range(self.cols):
                row_m_result.append(self.data[i][j] + m2.data[i][j])

            m_result.append(row_m_result)
        
        return Matrix(m_result)

    def __mul__(self, m2):
        # Matrix (not only) mulpiplication
        
        if self.cols != m2.rows:
            raise ValueError('Number of columns in the first matrix must be equal to the number of rows in the second matrix for matrix multiplication')
        
        m_result = []
            
        for i in range(self.rows):
            row_m_result = []
            for j in range(m2.cols):
                val_res = 0
                for k in range(self.cols):
                    val_res += self.data[i][k] * m2.data[k][j]

                row_m_result.append(val_res)
                
            m_result.append(row_m_result)
            
        return Matrix(m_result)

    def __matmul__(self, m2):
        # Hadamard product
        
        if (self.cols != m2.cols) or (self.rows != m2.rows):
            raise ValueError("Dimensions of two matrices must be same for Hadamard product")
        
        m_result = []
        
        for i in range(self.rows):
            row_m_result = []
            for j in range(self.cols):
                row_m_result.append(self.data[i][j] * m2.data[i][j])
                
            m_result.append(row_m_result)
        
        return Matrix(m_result)

    def save_file(self, filename):
        with open(filename, 'w') as f:
            for row in self.data:
                f.write(' '.join(map(str, row)) + '\n')

