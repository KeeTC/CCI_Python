# Assume you have method isSubString which checks if one string is a substring of another
# Given two strings, S1 and S2, write code to check if S2 is a rotation of S1 using only one call to isSubString

s1 = "waterbottle"
s2 = "orbottlewat"

def isSubString(s1,s2):
	return True if s2 in s1 else False

def isRotation(s1,s2):
	if len(s1) != len(s2):
		return False
	else:
		s1 += s2
		return isSubString(s1,s2)

print isRotation(s1,s2)