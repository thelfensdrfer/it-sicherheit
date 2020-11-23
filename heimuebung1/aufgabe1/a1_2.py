import random
import string

from heimuebung1.aufgabe1.a1_1 import H


def create_table(chars):
    out = {}
    for char in chars:
        out[char] = H(char)

    return out


def random_replacement(choices, original):
    # Get the original hash
    y = H(original)

    y_replacement = []
    for i in y[2:]:
        # Get the binary string for every char
        i = str(bin(int(i, 2)))

        # Get random char for the same binary string
        y_replacement.append(random.choice(choices[i]))

    return ''.join(y_replacement)



if __name__ == '__main__':
    word = 'BLACKBOX'
    table = create_table(list(string.ascii_uppercase))

    choices = {
        '0b0': [],
        '0b1': []
    }
    for char in table.keys():
        choices[str(table[char])].append(char)

    replacement = random_replacement(choices, word)

    print('Hash of {}: {}'.format(word, H(word)))
    print('Hash of {}: {}'.format(replacement, H(replacement)))
    print('Equal: {}'.format(H(word) == H(replacement)))
