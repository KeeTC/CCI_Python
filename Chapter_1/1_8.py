# Algorithm to zerofy MXN matrix

from copy import deepcopy

matrix = [[1, 1, 1],
		  [0, 1, 0],
		  [1, 0, 1,],
		 ]
# Zeroes entire row of array

def zerofy(mat):
	firstRowHasZeros = False
	firstColHasZeros = False

	# Check if first column has any zeros
	for i in range(0, len(mat)):
		if mat[i][0] == 0:
			firstColHasZeros = True

	#Check if first row has any zeros
	for i in range(0, len(mat[0])):
		if mat[0][i] == 0:
			firstRowHasZeros = True

	# Check rest of matrix for zeros, work the row and column using first row and column
	for i in range(1, len (mat)):
		for j in range(1, len(mat[0])):
			if mat[i][j] == 0:
				mat[0][j] = 0
				mat[i][0] = 0

	# Zerofy the marked columns and rows
	for i in range(0, len(mat[0])):
		if mat[0][i] == 0:
			for j in range(1, len(mat)):
				mat[j][i] = 0

	# Zero first column and row if necessary
	if firstRowHasZeros:
		for i in range(0, len(mat[0])):
			mat[i][0] = 0 

	return mat

print zerofy(matrix)
































