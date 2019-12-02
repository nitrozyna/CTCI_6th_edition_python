def palindromePermutation(string):
    char_dict = {}

    for char in string:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    found_odd = False
    # check no more than one character is odd
    for key, value in char_dict.items():
        if value % 2 == 1:
            # more than one value has an odd count
            if found_odd:
                return False
            found_odd = True
    return True


print(palindromePermutation("dfcfwdc"))