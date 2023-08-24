import numpy as np
import sympy as sp


def calculate_cofactors(matrix):
	n = len(matrix)
	cofactor_matrix = np.zeros_like(matrix)
	for i in range(n):
		for j in range(n):
			minor_matrix = np.delete(np.delete(matrix, i, axis = 0), j, axis = 1)
			cofactor_matrix[i, j] = (-1) ** (i + j) * np.linalg.det(minor_matrix)
	return cofactor_matrix


def calculate_inverse(matrix):
	determinant = np.linalg.det(matrix)
	if determinant == 0:
		raise ValueError("Matrix is singular, inverse does not exist")
	cofactor_matrix = calculate_cofactors(matrix)
	adjugate_matrix = cofactor_matrix.T
	inverse_matrix = adjugate_matrix / determinant
	return inverse_matrix


def main():
	# Replace this with your actual matrix
	input_matrix = np.array([
		[3, -4, 1, 2],
		[-2, -5, 0, -3],
		[4, 1, -1, 2],
		[1, 3, 0, -5]
	])
	
	determinant = np.linalg.det(input_matrix)
	cofactor_matrix = calculate_cofactors(input_matrix)
	inverse_matrix = calculate_inverse(input_matrix)
	
	print("Input Matrix:")
	print(input_matrix)
	print("\nDeterminant:", determinant)
	
	print("\nCofactor Matrix:")
	print(cofactor_matrix)
	
	print("\nInverse Matrix (as rational numbers):")
	for row in inverse_matrix:
		rational_row = [sp.Rational(num).limit_denominator() for num in row]
		print(rational_row)


if __name__ == "__main__":
	main()
