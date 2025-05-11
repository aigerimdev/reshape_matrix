from reshape_matrix.main import reshape_matrix
def test_convert_two_by_two_to_one_by_four():
    matrix = [[1,2],[3,4]]
    r = 1
    c = 4

    reshaped_matrix = reshape_matrix(matrix, r, c)

    assert reshaped_matrix == [[1,2,3,4]]

def test_cannot_reshape():
    matrix = [[1,2],[3,4]]
    r = 2
    c = 4

    reshaped_matrix = reshape_matrix(matrix, r, c)

    assert reshaped_matrix == [[1,2],[3,4]]

def test_convert_four_by_two_to_two_by_four():
    matrix = [[1,2],[3,4],[5,6],[7,8]]
    r = 2
    c = 4

    reshaped_matrix = reshape_matrix(matrix, r, c)

    assert reshaped_matrix == [[1,2,3,4],[5,6,7,8]]

def test_three_by_three_to_nine_by_one():
        # Arrange
        matrix = [[7, 2, 1], [4,3,5], [6,9,8]]
        r = 9
        c = 1 
        # Act
        answer = reshape_matrix(matrix, r, c)
        # Assert
        assert answer == [[7],[2],[1],[4],[3],[5],[6],[9],[8]]
        
# my test cases

# example input 1: [[1,2], [3,4], [5,6], [7,8]]
#                  r = 2, c = 4
# expected output 1: [[1, 2, 3, 4]], [5, 6, 7, 8]]

# example input 2: [[1, 2], [3, 4]]
#                  r = 3, c = 3
# expected output 2: [[1, 2], [3, 4]]

# example input 3: [[]]
#                  r = 0, c = 0
# expected output 3: []

# example input 4: [[1, 2], [3, 4]]
#                  r = 2, c = 2
# expected output 4: [[1, 2], [3, 4]]

# example input 5: [[1, 2]]
#                  r = 0, c = 2
# expected output 5: [1, 2]

# example input 6: [[1], [2], [3]]
#                  r = 1, c = 3
# expected output 6: [1, 2, 3]


def test_reshape_empty_matrix_returns_empty():
    # arrange
    matrix = []
    r = 0
    c = 0
    # act
    answer = reshape_matrix(matrix, r, c)
    # assert
    assert answer == []

def test_reshape_invalid_dimensions_returns_original():
    # arrange
    matrix = [[1, 2], [3, 4]]
    r = 3
    c = 3
    # act
    answer = reshape_matrix(matrix, r, c)
    # assert
    assert answer == [[1, 2], [3, 4]]

def test_reshape_single_row_to_square():
    # arrange
    matrix = [[1, 2, 3, 4]]
    r = 2
    c = 2
    # act
    answer = reshape_matrix(matrix, r, c)
    # assert
    assert answer == [[1, 2], [3, 4]]

def test_reshape_single_column_to_row():
    # arrange
    matrix = [[1], [2], [3]]
    r = 1
    c = 3
    # act
    answer = reshape_matrix(matrix, r, c)
    # assert
    assert answer == [[1, 2, 3]]

def test_reshape_same_shape_returns_same():
    # arrange
    matrix = [[1, 2], [3, 4]]
    r = 2
    c = 2
    # act
    answer = reshape_matrix(matrix, r, c)
    # assert
    assert answer == [[1, 2], [3, 4]]

def test_reshape_single_element():
    # arrange
    matrix = [[1]]
    r = 1
    c = 1
    # act
    answer = reshape_matrix(matrix, r, c)
    # assert
    assert answer == [[1]]

def test_reshape_to_single_row():
    # arrange
    matrix = [[1], [2], [3]]
    r = 1
    c = 3
    # act
    answer = reshape_matrix(matrix, r, c)
    # assert
    assert answer == [[1, 2, 3]]

def test_reshape_to_single_column():
    # arrange
    matrix = [[1, 2, 3]]
    r = 3
    c = 1
    # act
    answer = reshape_matrix(matrix, r, c)
    # assert
    assert answer == [[1], [2], [3]]

def test_reshape_larger_matrix_to_2_by_4():
    # arrange
    matrix = [[1,2], [3,4], [5,6], [7,8]]
    r = 2
    c = 4
    # act
    answer = reshape_matrix(matrix, r, c)
    # assert
    assert answer == [[1, 2, 3, 4], [5, 6, 7, 8]]
