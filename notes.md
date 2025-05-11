Ask clarifying questions:

What if the dimensions don't match ([[1, 2], [3, 4]], 3, 3)?
– It should return the original matrix.

What if the matrix is empty ([], 0, 0)?
– It should return an empty list because there is no data to reshape, and the program should still run without crashing.

What if there is only one row, like: ([[1, 2, 3, 4]], 2, 2)?
– It should still work as a two-dimensional matrix.

What if there is only one column, like: ([[1], [2], [3]], 1, 3)?
– It should also work as a two-dimensional matrix.

What if the number of rows or columns is 0, like: ([[1, 2]], 0, 2)?
– It should return the original matrix, since reshaping isn't valid.


Pseudocode:

Define a function called reshape_matrix which takes three parameters: matrix, r, c

1. Count total items:
- Create a variable called total_items and set it to 0
- Loop through each row in the matrix
- For each row, get its length and add it to total_items

2. Check if reshape is possible:
- If total_items is equal to r * c, continue
- Otherwise, return the original matrix

3. Flatten the matrix:
- Use list comprehension to loop through each row
  - loop through each number in the row
  - Collect all numbers into flat_list

4. Build the new matrix:
- Create an empty list called new_matrix
- Set index = 0
- Loop r times (for each row)
  - Inside, create an empty list called row
  - Loop c times (for each column)
    - Append flat_list[index] to row
    - Increase index by 1
  - Append row to new_matrix
5. Return new_matrix
