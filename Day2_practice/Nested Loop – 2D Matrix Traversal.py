# Given a 2D matrix, print each element using a nested for loop.

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j],end=" ")
    print()