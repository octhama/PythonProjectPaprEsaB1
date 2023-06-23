import unittest

from ExamenAlgoProgHaslerTehouESAJuin2023.modules.VerifNumNat import verifnatnumfich, verifsexe, nbre_nat


class TestVerifnatnumfich(unittest.TestCase):
	#  Tests that the function successfully opens and reads the input file
	def test_valid_file(self):
		# Arrange
		expected = True
		
		# Act
		try:
			verifnatnumfich()
		except FileNotFoundError:
			actual = False
		else:
			actual = True
		
		# Assert
		self.assertEqual(expected, actual)
	
	#  Tests that the input file contains valid national numbers
	def test_valid_national_numbers(self):
		# Arrange
		expected = ["97010100178", "97010100179", "97010100180"]
		
		# Act
		verifnatnumfich()
		with open("resources/numNatOk.csv", "r") as f:
			actual = f.read().splitlines()
		
		# Assert
		self.assertEqual(expected, actual)
	
	#  Tests that the function successfully creates and writes to the output file
	def test_create_output_file(self):
		# Arrange
		expected = True
		
		# Act
		verifnatnumfich()
		try:
			with open("resources/numNatOk.csv", "r") as f:
				f.read()
		except FileNotFoundError:
			actual = False
		else:
			actual = True
		
		# Assert
		self.assertEqual(expected, actual)
	
	#  Tests that the function handles an empty input file
	def test_empty_file(self):
		# Arrange
		expected = []
		
		with open("resources/empty_file.data", "w") as f:
			pass
		
		# Act
		verifnatnumfich()
		with open("resources/numNatOk.csv", "r") as f:
			actual = f.read().splitlines()
		
		# Assert
		self.assertEqual(expected, actual)
	
	#  Tests that the function handles an input file containing only invalid national numbers
	def test_invalid_national_numbers(self):
		# Arrange
		expected = []
		
		with open("resources/invalid_national_numbers.data", "w") as f:
			f.write("12345678901\n23456789012\n34567890123\n")
		
		# Act
		verifnatnumfich()
		with open("resources/numNatOk.csv", "r") as f:
			actual = f.read().splitlines()
		
		# Assert
		self.assertEqual(expected, actual)
	
	#  Tests that the function handles an input file containing a mix of valid and invalid national numbers
	def test_mixed_national_numbers(self):
		# Arrange
		expected = ["97010100178", "97010100179", "97010100180"]
		
		with open("resources/mixed_national_numbers.data", "w") as f:
			f.write("12345678901\n97010100178\n23456789012\n97010100179\n34567890123\n97010100180\n")
		
		# Act
		verifnatnumfich()
		with open("resources/numNatOk.csv", "r") as f:
			actual = f.read().splitlines()
		
		# Assert
		self.assertEqual(expected, actual)
	
	#  Tests that the function reads the input file successfully
	def test_happy_path_read_input_file(self):
		verifsexe()
		with open("resources/numNatOk.csv", "r") as f:
			content = f.readlines()
		self.assertTrue(len(content) > 0)
	
	#  Tests that the function writes the output file successfully
	def test_happy_path_write_output_file(self):
		verifsexe()
		with open("resources/numNatOkAndSexe.csv", "r") as f:
			content = f.readlines()
		self.assertTrue(len(content) > 0)
	
	#  Tests that the function correctly identifies the gender of the national numbers
	def test_happy_path_identify_gender(self):
		verifsexe()
		with open("resources/numNatOkAndSexe.csv", "r") as f:
			content = f.readlines()
		for line in content:
			gender = line.split()[-1]
			self.assertIn(gender, ["M", "F"])
	
	#  Tests that the function handles an empty input file
	def test_edge_case_empty_input_file(self):
		with open("resources/empty.csv", "w") as f:
			f.write("")
		verifsexe()
		with open("resources/numNatOkAndSexe.csv", "r") as f:
			content = f.readlines()
		self.assertEqual(len(content), 0)
	
	#  Tests that the function handles an input file with only one line
	def test_edge_case_one_line_input_file(self):
		with open("resources/one_line.csv", "w") as f:
			f.write("12345678901")
		verifsexe()
		with open("resources/numNatOkAndSexe.csv", "r") as f:
			content = f.readlines()
		self.assertEqual(len(content), 1)
	
	#  Tests that the function handles an input file with only invalid national numbers
	def test_edge_case_invalid_national_numbers(self):
		with open("resources/invalid.csv", "w") as f:
			f.write("1234567890\n123456789012\n1234567890a\n")
		verifsexe()
		with open("resources/numNatOkAndSexe.csv", "r") as f:
			content = f.readlines()
		self.assertEqual(len(content), 0)
	
	def test_valid_and_invalid_count(self):
		nbre_nat()
		# Check that the function prints the correct number of valid and invalid national numbers
		with open("resources/num_nat.data", "r") as f:
			lines = f.readlines()
			valid_count = sum(1 for line in lines if
							  len(line.strip("\n")) == 11 and int(line.strip("\n")[9:11]) == 97 - int(
								  line.strip("\n")[0:9]) % 97)
			invalid_count = len(lines) - valid_count
		self.assertEqual(valid_count, 4)
		self.assertEqual(invalid_count, 2)
	
	#  Tests that the function handles an empty file
	def test_empty_file(self):
		with open("resources/empty_file.data", "w") as f:
			pass
		nbre_nat()
		# Check that the function prints 0 for both valid and invalid national numbers
		self.assertEqual(nat_ok, 0)
		self.assertEqual(nat_ko, 0)
	
	#  Tests that the function handles a file containing only invalid national numbers
	def test_only_invalid_numbers(self):
		with open("resources/invalid_numbers.data", "w") as f:
			f.write("12345678901\n23456789012\n34567890123\n")
		nbre_nat()
		# Check that the function prints the correct number of invalid national numbers
		self.assertEqual(nat_ko, 3)
	
	#  Tests that the function handles a file containing only valid national numbers
	def test_only_valid_numbers(self):
		with open("resources/valid_numbers.data", "w") as f:
			f.write("12345678901\n23456789012\n34567890123\n")
			f.write("45678901234\n56789012345\n67890123456\n")
		nbre_nat()
		# Check that the function prints the correct number of valid national numbers
		self.assertEqual(nat_ok, 6)
	
	#  Tests that the function handles a file not found error
	def test_file_not_found(self):
		with self.assertRaises(FileNotFoundError):
			nbre_nat("resources/nonexistent_file.data")
	
	#  Tests that the function handles an invalid file format error
	def test_invalid_file_format(self):
		with open("resources/invalid_format.txt", "w") as f:
			f.write("12345678901\n23456789012\n34567890123")
		with self.assertRaises(ValueError):
			nbre_nat()
