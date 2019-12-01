def checkPermutation(string_one, string_two):
    char_d1, char_d2 = {}, {}

    if len(string_one) != len(string_two):
        return False
    else:
        for char in char_d1:
            char_d1[char] += 1
        for char in char_d2:
            char_d2[char] += 1

    if set(char_d1.keys()) == set(char_d2.keys()):
        return set(char_d1.values()) == set(char_d2.values())
    else:
        return False

#print(checkPermutation("gosialubimisie","eisimibulaisog"))