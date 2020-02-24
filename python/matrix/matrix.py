class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = []
        # Split in lines
        self._tmp_matrix_lines = matrix_string.splitlines()

        # split values
        self._tmp_matrix_split = [x.split(' ') for x in self._tmp_matrix_lines]

        # Convert values to integer
        self._tmp_matrix_converter = []
        for line in self._tmp_matrix_split:
            for value in line:
                self._tmp_matrix_converter.append(int(value))
            self.matrix.append(self._tmp_matrix_converter.copy())
            self._tmp_matrix_converter.clear()


    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [column[index - 1] for column in self.matrix]
