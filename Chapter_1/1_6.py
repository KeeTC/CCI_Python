# Implement a method to perform basic string compression using the counts of repeated characters method

def compress(str1):
	res = [] 
	cnt = 0
	prev = str1[0]

	for char in str1:
		if char == prev:
			cnt += 1
		else:
			res += prev + str(cnt)
			prev = char
			cnt = 1
	res += prev + str(cnt)
	res = ''.join(res)
	if len(res) < len(str1): return res
	else: return str1

print compress ("aabccccaaa")
