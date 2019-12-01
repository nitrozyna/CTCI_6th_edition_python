def isUnique(characters):
    char_dict = {}
    for char in characters:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            return False
    return True


# print(isUnique("sdfGd"))


