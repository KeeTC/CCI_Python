# Writer a function to check if a string is a permutation of a palindrome

import string 

def isPermutationOfPalindrome(str):
	d = dict.fromkeys(string.ascii_lowercase, False)
	count = 0
	for char in str:
		if (ord(char) > 97 and ord(char) < 123):
			d[char] = not d[char]
	for key in d:
		if d[key] is True:
			count += 1
			if count > 1:
				return False
		return True

print isPermutationOfPalindrome("aa bb cc eee f")