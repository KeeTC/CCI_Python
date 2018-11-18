# Given an image represented by an NxN matrix, Write a method to rotate the image by 90 degrees.
# Time Complexity - 0(n^2) (2 for loops looping through the entire input matrix for each element)

from copy import deepcopy

def rotateMatrix(matrix, n):
	res = deepcopy(matrix) # res will be our original matrix rotated 90 degrees
	for x in range (0, n):
		for y in range(n-1, -1, -1):
			res[x][n-y-1] = matrix[y][x]
	return res

n = 3
matrix = [[1,2,3], [4,5,6], [7,8,9]]
#res =	 [[_,_,_], [_,_,_], [_,_,_]]
print "Original Matrix: " + str(matrix)
print "Rotated Matrix:  " + str(rotateMatrix(matrix, n))