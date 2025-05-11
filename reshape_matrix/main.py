def reshape_matrix(matrix, r, c):
    '''
    INPUT: 2D list `matrix`, and integers `r` (rows) and `c` (columns)
    OUTPUT: Reshaped matrix if possible, otherwise original matrix
    '''
    # Count total elements
    total_items = 0
    for row in matrix:
        total_items+= len(row)
    
    # Check if reshape is possible
    if total_items != r * c:
        return matrix

    # Flatten with list comprehension
    flat_list = [num for row in matrix for num in row]
    
    # Build new matrix
    new_matrix = []
    index = 0
    for i in range(r):
        row = []
        for j in range(c):
            row.append(flat_list[index])
            index += 1
        new_matrix.append(row)
    return new_matrix