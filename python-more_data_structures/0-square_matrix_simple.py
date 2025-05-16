#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    for row in matrix:
        squared_row = []
        for num in row:
            squared_row.append(num ** 2)
        squared.append(squared_row)
    return squared
