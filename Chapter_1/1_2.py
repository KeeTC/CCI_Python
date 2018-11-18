# Test if two strings are permutations of one another

# def checkPermutation(str1, str2):
# 	if len(str1) != len(str2): return False
# 	else: return ''.join(sorted(str1)) == ''.join(sorted(str2))

# print checkPermutation("abdc", "bcca")

def pair_sum(arr,k):

    if len(arr)<2:
        return

    # Sets for tracking
    seen = set()
    output = set()

    for num in arr:

        target = k-num

        if target not in seen:
            seen.add(num)

        else:
            output.add(((min(num, target)), max(num, target)))

    print(output)



pair_sum([1, 3, 2, 2], 4)