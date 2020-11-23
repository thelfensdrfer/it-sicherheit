def H(input):
    i = 0
    y = {}

    for h_i in input:
        # Convert h_i to ascii and the ascii number to binary
        h_i = bin(ord(h_i))

        # Get a list of binary values
        y_i = list(h_i)[2:]

        # Pad the list with values to always get 8 bits
        y_i.reverse()
        y_i.extend((8 - len(y_i)) * [0])
        y_i.reverse()

        # Convert 0 and 1 to integers
        y_i = list(map(lambda x: int(x), y_i))

        # XOR values
        y[i] = y_i[0] ^ y_i[1] ^ y_i[2] ^ y_i[3] ^ y_i[4] ^ y_i[5] ^ y_i[6] ^ y_i[7]

        i = i + 1

    # Convert y dictionary to binary number
    return bin(int('0b' + ''.join(str(x) for x in dict.values(y)), 2))


if __name__ == '__main__':
    y = H('BLACKBOX')
    print(y)
