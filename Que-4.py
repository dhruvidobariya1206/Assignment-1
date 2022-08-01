# rite a Python program which takes two digits m (row) and n (column) as input and
# generates a two dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
# Input
# Input number of rows: 3 
# Input number of columns: 4 
# Output
# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]


rows = int(input("Enter number of rows:"))
cols = int(input("Enter number of columns:"))
arr = []
for i in range(rows):
    column = []
    for j in range(cols):
        column.append(i*j)
    arr.append(column)
print(arr)