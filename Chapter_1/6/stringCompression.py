def stringCompression(string):
    compressed = []
    counter = 0

    for i in range(len(string)):
        if i != 0 and string[i] != string[i - 1]:
            print(i)
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1
    compressed.append(string[-1] + str(counter))
    return min(string, ''.join(compressed), key=len)

print(stringCompression('fwwffdwff'))