# QUESTION: Implement an algorithm to determine if a string has all unique characters.

# Assuming ASCII (non-extended) 128 max unique characters

def uni_char2(str):

	if len(str) > 128: return False

	char = set()

	for var in str:
		if var in char:
			return False
		else:
			char.add(var)
			return True

uni_char2('abc')